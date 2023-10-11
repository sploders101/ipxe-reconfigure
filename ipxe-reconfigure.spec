Name:           ipxe-reconfigure
Version:        0.4
Release:        1%{?dist}
Summary:        Reconfigures the ipxe boot script upon kernel update

License:        Unlicense
URL:            N/A
Source0:        %{name}-%{version}.tar.gz

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
install -m 0755 ipxe-reconfigure $RPM_BUILD_ROOT/%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/kernel/install.d
install -m 0755 99-ipxe-reconfigure.install ${RPM_BUILD_ROOT}/usr/lib/kernel/install.d/99-ipxe-reconfigure.install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/ipxe-reconfigure
/usr/lib/kernel/install.d/99-ipxe-reconfigure.install

%changelog
* Fri Oct 06 2023 Shaun Keys <mariobuddy@gmail.com> 0.4-1
- 

* Fri Oct 06 2023 Shaun Keys <mariobuddy@gmail.com> 0.3-1
- new package built with tito

* Mon Sep 25 2023 Shaun Keys
- 
