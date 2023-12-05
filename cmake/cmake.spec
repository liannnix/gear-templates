%define _unpackaged_files_terminate_build 1

Name:      $module
Version:   $version
Release:   alt1

Summary:   $summary
#Summary(ru_RU.UTF-8):
License:   $license
Group:     Other
Url:       $url

Source:    %name-%version.tar
#Patch:     %name-%version-alt.patch

#BuildArch: x86_64
#ExcludeArch: %arm

BuildRequires(pre): rpm-macros-cmake
#BuildRequires: cmake
#BuildRequires: gcc-c++

#%%add_findreq_skiplist %_datadir/%name/*
#%%add_findprov_skiplist */%name/nginx.pm

%description
$description

#%%description -l ru_RU.UTF-8

#%%package
#%%package -n fullname

%prep
%setup
#%%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install
#%%__cat <<EOF >>%buildroot/file
#text
#EOF
%find_lang %name

%check

%files -f %name.lang
%doc *.md
#%config(noreplace) %_sysconfdir/%name.conf
#%attr(600,root,root) %config(noreplace) %_sysconfdir/%name.conf
#%dir %_libdir/%name
#%exclude %_bindir/trash
%_bindir/*
%_man1dir/*

#%%files -n fullname

%changelog
$stamp-alt1
$lastchange
