from requests_html import HTMLSession
from distutils.version import StrictVersion
import json
from config import DOWNLOAD_PATH
import os

validate_versions_commands = ['install', 'uninstall', 'use']


def list_local(args):
    program = args.program
    dest_path = DOWNLOAD_PATH

    """ lists installed kubectl/kustomize/helm versions """

    available_versions = []
    for f_name in os.listdir(DOWNLOAD_PATH):
        if f_name.startswith(program):
            version = f_name.split('_')[1]
            available_versions.append(version)

    if args.commands in validate_versions_commands:
        return available_versions

    for version in available_versions:
        print(version)


def list_remote(args):
    program = args.program

    """ lists kubectl/kustomize/helm/helmfile versions """

    if program == "kubectl":
        page = 1
        elements = -1
        available_versions = ['']
        while elements != 0:
            session = HTMLSession()
            kustomize_url = session.get(
                f"https://api.github.com/repos/kubernetes/kubectl/tags?per_page=100&page={page}")
            data = kustomize_url.html.full_text
            parsed_json = (json.loads(data))
            elements = len(parsed_json)
            for version in parsed_json:
                try:
                    if "v0" not in version['name'] and "rc" not in version['name'] and "beta" not in version[
                        'name'] and "alpha" not in version['name']:
                        available_versions.append(version['name'].lstrip('kubernetes-'))
                except IndexError:
                    raise Exception("Github rate limiting!!")
            page += 1
        available_versions.remove('')

        if args.commands in validate_versions_commands:
            return available_versions

        for version in available_versions:
            print(version)

    elif program == "kustomize":
        session = HTMLSession()
        kustomize_url = session.get(
            "https://api.github.com/repos/kubernetes-sigs/kustomize/tags?per_page=1000")
        data = kustomize_url.html.full_text
        parsed_json = (json.loads(data))
        available_versions = ['']

        for version in parsed_json:
            try:
                if "v3.3.0" not in version['name'] and "v3.3.1" not in version['name'] and "v1.0.0" not in version[
                    'name'] and "kyaml" not in version['name'] and "pseudo" not in version['name'] and "api" not in \
                        version['name'] and "latest_kustomize" not in version['name'] and "pluginator" not in \
                        version['name'] and "cmd" not in version['name'] and "kstatus" not in version['name']:
                    available_versions.append(version['name'])
            except IndexError:
                raise Exception("Github rate limiting!!")

        available_versions.remove('')

        if args.commands in validate_versions_commands:
            return available_versions

        for version in available_versions:
            print(version)

    elif program == "helm":
        session = HTMLSession()
        helm_url = session.get(
            "https://api.github.com/repos/helm/helm/tags?per_page=1000")
        data = helm_url.html.full_text
        parsed_json = (json.loads(data))
        available_versions = ['']

        for version in parsed_json:
            try:
                if "rc" not in version['name'] and "beta" not in version['name'] and "alpha" not in version['name']:
                    available_versions.append(version['name'])
            except IndexError:
                raise Exception("Github rate limiting!!")

        available_versions.remove('')

        if args.commands in validate_versions_commands:
            return available_versions

        for version in available_versions:
            print(version)

    elif program == "helmfile":
        session = HTMLSession()
        helmfile_url = session.get(
            "https://api.github.com/repos/roboll/helmfile/tags?per_page=1000")
        data = helmfile_url.html.full_text
        parsed_json = (json.loads(data))
        available_versions = ['']

        for version in parsed_json:
            try:
                if "0.89.1" not in version['name'] and "0.81.2" not in version['name'] and "rc" not in version[
                    'name'] and "beta" not in version['name'] and "alpha" not in version['name']:
                    available_versions.append(version['name'])
            except IndexError:
                raise Exception("Github rate limiting!!")

        available_versions.remove('')

        if args.commands in validate_versions_commands:
            return available_versions

        for version in available_versions:
            print(version)
    else:
        raise Exception(
            'Invalid Argument !! It should be either kubectl / kustomize / helm / helmfile')
