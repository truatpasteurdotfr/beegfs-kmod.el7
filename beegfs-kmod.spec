# Define the kmod package name here.
%define kmod_name beegfs

# If kversion isn't defined on the rpmbuild line, define it here.
%{!?kversion: %define kversion 3.10.0-229.el7.%{_target_cpu}}

Name:    %{kmod_name}-kmod
Version: 2015.03.r7
Release: 1%{?dist}
Group:   System Environment/Kernel
License: GPLv2
Summary: %{kmod_name} kernel module(s)
URL:     http://www.beegfs.com

BuildRequires: perl
BuildRequires: redhat-rpm-config
ExclusiveArch: x86_64

# Sources.
# rpm2cpio beegfs-client-2015.03.r7-el6.noarch.rpm | cpio -iudv
# cd opt/beegfs/src/client && tar cjvf beegfs-2015.03.r7.tar.bz2 beegfs_client_module_2015.03
Source0:  %{kmod_name}-%{version}.tar.bz2
Source5:  GPL-v2.0.txt
Source10: kmodtool-%{kmod_name}-el7.sh

# Magic hidden here.
%{expand:%(sh %{SOURCE10} rpmtemplate %{kmod_name} %{kversion} "")}

# Disable the building of the debug package(s).
%define debug_package %{nil}

%description
This package provides the %{kmod_name} kernel module(s).
It is built to depend upon the specific ABI provided by a range of releases
of the same variant of the Linux kernel and not on any one specific build.

This package contains binary objects of the closed source part of BeeGFS and
open source code to allow to build the client kernel module.

%prep
%setup -q -n beegfs_client_module_2015.03
echo "override %{kmod_name} * weak-updates/%{kmod_name}" > kmod-%{kmod_name}.conf

%build
KSRC=%{_usrsrc}/kernels/%{kversion}
%{__make} -C build %{?_smp_mflags} KVERSION=%{kversion} KDIR=/usr/src/kernels/%{kversion} 
#%{__make} -C "${KSRC}" %{?_smp_mflags} modules M=$PWD

%install

%{__install} -D -m 644 build/%{kmod_name}.ko %{buildroot}/lib/modules/%{kversion}/extra/%{kmod_name}/%{kmod_name}.ko
%{__install} -d %{buildroot}%{_sysconfdir}/depmod.d/
%{__install} kmod-%{kmod_name}.conf %{buildroot}%{_sysconfdir}/depmod.d/
%{__install} -d %{buildroot}%{_defaultdocdir}/kmod-%{kmod_name}-%{version}/
%{__install} %{SOURCE5} %{buildroot}%{_defaultdocdir}/kmod-%{kmod_name}-%{version}/

%clean
%{__rm} -rf %{buildroot}

%changelog
* Wed Nov 18 2015 Tru Huynh <tru@pasteur.fr> - 2015.03.r7
- Initial el7 build of the kmod package.
- Source code extracted from the beegfs-client-2015.03.r7-el6.noarch.rpm 
  at http://www.beegfs.com/release/beegfs_2015.03/dists/rhel6
  (identical for rhel7 version)
