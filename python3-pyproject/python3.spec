%define _unpackaged_files_terminate_build 1
%define pypi_name $module
%define mod_name $module

%def_without check

Name:    python3-module-%pypi_name
Version: $version
Release: alt1

Summary: $summary
License: $license
Group:   Development/Python3
URL:     $url
#VCS:     $url

BuildRequires(pre): rpm-build-pyproject
# Sphinx documentation
#BuildRequires: python3-module-sphinx

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

#BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

#Provides: %pypi_name = %EVR
#%%py3_provides %pypi_name

BuildArch: noarch

Source: %pypi_name-%version.tar
#Source1: %pyproject_deps_config_name

#Patch: %pypi_name-%version-alt.patch

%description
$description

%prep
%setup -n %pypi_name-%version
#%%patch -p1
# hack for setuptools_scm
#%%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

# Sphinx documentation
#%%make -C docs html SPHINXBUILD=sphinx-build-3

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject
#%%pyproject_run_pytest -ra tests

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
#%%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
$stamp-alt1
$lastchange
