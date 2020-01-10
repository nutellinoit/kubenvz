[![Actions Status](https://github.com/nutellinoit/kubenvz/workflows/Build%20&%20Release/badge.svg)](https://github.com/nutellinoit/kubenvz/actions)
# kubenvz

kubectl & kustomize version control

Inspired by terraenv https://github.com/aaratn/terraenv

## Installation

### Automatic

Install via Homebrew on OSx

```console
$ brew tap nutellinoit/kubenvz
$ brew install kubenvz
```
### Upgrade

via Homebrew on OSx

```console
$ brew upgrade kubenvz
```


## Usage

### kubenvz <kubectl / kustomize > install [version]

Install a specific version of kubectl. Available options for version:

- `1.2.3` exact version to install


```console
$ kubenvz kubectl install 1.16.0
$ kubenvz kustomize install 1.0.10
```

## LICENSE

- [kubenvz](https://github.com/aaratn/kubenvz/blob/master/LICENSE)
- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [rbenv](https://github.com/rbenv/rbenv/blob/master/LICENSE)

## Inspiration

- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [tfenv](https://github.com/tfutils/tfenv)
- [tgenv](https://github.com/cunymatthieu/tgenv)
- [rbenv](https://github.com/rbenv/rbenv)
