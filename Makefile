PLATFORM?=linux_x64

.PHONY: build package test-kubectl test-kustomize test-helm test-all

build:
	@PYTHONOPTIMIZE=1 pyinstaller kubenvz.py --onefile --clean --osx-bundle-identifier com.nutellinoit.os.kubenvz --nowindowed
	@chmod +x dist/kubenvz

package:
	@cd dist && tar -czvf ./kubenvz_$(PLATFORM).tar.gz kubenvz

test-kustomize:
	rm -rf ~/.kubenvz/kustomize*
	dist/kubenvz kustomize list remote | sort | xargs -n 1 -P 1 dist/kubenvz kustomize install -f

test-kubectl:
	rm -rf ~/.kubenvz/kubectl*
	dist/kubenvz kubectl list remote | sort | xargs -n 1 -P 1 dist/kubenvz kubectl install -f

test-helm:
	rm -rf ~/.kubenvz/helm*
	dist/kubenvz helm list remote | sort | xargs -n 1 -P 1 dist/kubenvz helm install -f

test-helmfile:
	rm -rf ~/.kubenvz/helmfile*
	dist/kubenvz helmfile list remote | sort | xargs -n 1 -P 1 dist/kubenvz helmfile install -f


test-all: test-kubectl test-helm test-helmfile test-kustomize