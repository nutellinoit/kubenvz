import os.path
import os
from dotenv import load_dotenv
import sys
import platform
import urllib
import tarfile
import requests
from zipfile import ZipFile
from config import DOWNLOAD_PATH, VERSION_FILE
from .list import list_remote

""" Download Required kubectl / kustomize / helm / helmfile Versions """


def download_program(args, program, version, fast):
    operating_sys = sys.platform
    # Upsert download path
    not os.path.exists(DOWNLOAD_PATH) and os.mkdir(DOWNLOAD_PATH)

    if not fast:
        available_versions = list_remote(args)
        if version not in available_versions:
            print("Version '" + version + "' is not right available " + program + " version.\
                \nYou can check right available versions by running 'kubenvz kubectl/kustomize list remote'.\n")
            sys.exit(1)
    else:
        print("Skipping remote check...")

    if program == "kubectl":
        url = "https://storage.googleapis.com/kubernetes-release/release/v" + version + "/bin/" + operating_sys + "/amd64/kubectl"
        alternative_url = url
        alternative_url_binary = url

    elif program == "helm":
        # https://get.helm.sh/helm-v3.1.0-darwin-amd64.tar.gz
        url = "https://get.helm.sh/helm-v" + version.lstrip("v") + "-" + operating_sys + "-amd64.tar.gz"
        alternative_url = url
        alternative_url_binary = url

    elif program == "helmfile":
        # https://github.com/roboll/helmfile/releases/download/v0.100.1/helmfile_darwin_amd64
        url = "https://github.com/roboll/helmfile/releases/download/v" + version.lstrip("v") + "/helmfile_" + operating_sys + "_amd64"
        alternative_url = url
        alternative_url_binary = url

    elif program == "kustomize" and "kustomize" not in version:
        url = "https://github.com/kubernetes-sigs/kustomize/releases/download/" + \
              version + "/kustomize_" + version.lstrip("v") + "_" + operating_sys + "_amd64"
        alternative_url = "https://github.com/kubernetes-sigs/kustomize/releases/download/" + \
                          version + "/kustomize_" + version.lstrip("v") + "_" + operating_sys + "_amd64.tar.gz"
        alternative_url_binary = url

    elif program == "kustomize" and "kustomize" in version:
        url = "https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2F" + \
              version.lstrip("kustomize/") + "/kustomize_" + version.lstrip(
            "kustomize/") + "_" + operating_sys + "_amd64.tar.gz"
        alternative_url = "https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2F" + \
                          version.lstrip("kustomize/") + "/kustomize_kustomize." + version.lstrip(
            "kustomize/") + "_" + operating_sys + "_amd64.tar.gz"
        alternative_url_binary = "https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2F" + \
                                 version.lstrip("kustomize/") + "/kustomize_kustomize." + version.lstrip(
            "kustomize/") + "_" + operating_sys + "_amd64"

    if not os.path.exists(DOWNLOAD_PATH + program + "_" + version.lstrip("kustomize/").lstrip("v")):

        print("Downloading", program, version, "from", url)

        binary = requests.get(url)

        if binary.status_code == 404:
            print("Retrying ", program, version, "from", alternative_url)
            url = alternative_url
            binary = requests.get(alternative_url)
            if binary.status_code == 404:
                print("Retrying ", program, version, "from", alternative_url_binary)
                url = alternative_url_binary
                binary = requests.get(alternative_url_binary)
                if binary.status_code == 404:
                    print("Error downloading", program, version, "from", url)
                    raise Exception("Invalid version, got 404 error !")

        dest_path = DOWNLOAD_PATH + program + "_" + version.lstrip("kustomize/").lstrip("v")

        print("Downloading to", dest_path)

        open(dest_path, 'wb').write(binary.content)

        if "tar.gz" in url:

            tar = tarfile.open(dest_path, "r:gz")
            tar.extractall(path=DOWNLOAD_PATH + '/')
            tar.close()

            if os.path.exists(DOWNLOAD_PATH + '/' + program) and os.path.exists(dest_path):
                os.remove(dest_path)
                os.rename(DOWNLOAD_PATH + '/' + program, dest_path)
            elif os.path.exists(DOWNLOAD_PATH + "/" + operating_sys + "-amd64/" + program) and os.path.exists(dest_path):
                os.remove(dest_path)
                os.rename(DOWNLOAD_PATH + "/" + operating_sys + "-amd64/" + program, dest_path)
            else:
                raise Exception("Issue extracting !!")

        os.chmod(dest_path, 0o755)
    else:
        print(program, version, "already downloaded")


""" Installs Required kubectl / kustomize / helm / helmfile Versions """


def install(args):
    program = args.program
    version = args.version
    fast = args.f

    if not version and os.path.exists(VERSION_FILE):
        load_dotenv(dotenv_path=VERSION_FILE)
        version = (os.getenv(program.upper()))

    if not version:
        print("Please define version or add that to .kubenvz file.\
            \nYou don't need to mention version if you have .kubenvz file at current path. \n")
        sys.exit(1)

    dest_path = DOWNLOAD_PATH + program + "_" + version.lstrip("kustomize/").lstrip("v")

    if program == "kubectl":
        download_program(args, program, version, fast)

    elif program == "kustomize":
        download_program(args, program, version, fast)

    elif program == "helm":
        download_program(args, program, version, fast)

    elif program == "helmfile":
        download_program(args, program, version, fast)

    else:
        raise Exception(
            'Invalid Arguement !! It should be either kubectl / kustomize / helm / helmfile')

    if not os.access('/usr/local/bin', os.W_OK):
        print("Error: User doesn't have write permission of /usr/local/bin directory.\
            \n\nRun below command to grant permission and rerun 'kubenvz install' command.\
            \nsudo chown -R $(whoami) /usr/local/bin\n")
        sys.exit(1)

    try:
        os.remove("/usr/local/bin/" + program)

    except FileNotFoundError:
        pass

    os.symlink(dest_path, "/usr/local/bin/" + program)
