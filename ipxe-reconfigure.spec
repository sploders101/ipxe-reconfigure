Name:           ipxe-reconfigure
Version:        0.2
Release:        1%{?dist}
Summary:        Reconfigures the ipxe boot script upon kernel update

License:        Unlicense
URL:            N/A
Source0:        ipxe-reconfigure.tar.gz

Requires:       bash

%description
Reconfigures the ipxe boot script upon kernel update

%global debug_package %{nil}

%prep
%autosetup


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp ipxe-reconfigure $RPM_BUILD_ROOT/%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/kernel/install.d
cp 99-ipxe-reconfigure.install ${RPM_BUILD_ROOT}/usr/lib/kernel/install.d/99-ipxe-reconfigure.install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/ipxe-reconfigure
/usr/lib/kernel/install.d/99-ipxe-reconfigure.install

%triggerin -- kernel-core
ipxe-reconfigure


%changelog
* Mon Sep 25 2023 Shaun Keys
- 
