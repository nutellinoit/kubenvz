PLATFORM?=linux_x64

.PHONY: build package test-kubectl test-kustomize

build:
	@PYTHONOPTIMIZE=1 pyinstaller kubenvz.py --onefile --clean --osx-bundle-identifier com.nutellinoit.os.kubenvz --nowindowed
	@chmod +x dist/kubenvz

package:
	@cd dist && tar -czvf ./kubenvz_$(PLATFORM).tar.gz kubenvz

test-kustomize:
	rm -rf ~/.kubenvz/kustomize*
	dist/kubenvz kustomize list remote | xargs -r -n 1 dist/kubenvz kustomize install

test-kubectl:
	rm -rf ~/.kubenvz/kubectl*
	dist/kubenvz kubectl list remote | xargs -r -n 1 dist/kubenvz kubectl install
