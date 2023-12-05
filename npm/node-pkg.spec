%define _unpackaged_files_terminate_build 1
%define node_module $module

Name:    node-%node_module
Version: $version
Release: alt1

Summary: $summary
License: $license
Group:   Other
URL:     $url
VCS:     $url

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs

Provides: nodejs-%node_module = %EVR

BuildArch: noarch

%description
$summary

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module/
#cp -a lib %buildroot%nodejs_sitelib/%node_module/
#cp -a index.js %buildroot%nodejs_sitelib/%node_module/
#cp -a package.json %buildroot%nodejs_sitelib/%node_module/

%check

%files
%doc *.md
%nodejs_sitelib/%node_module

%changelog
$stamp-alt1
$lastchange
