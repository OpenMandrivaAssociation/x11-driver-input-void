Name: x11-driver-input-void
Version: 1.1.1
Release: %mkrel 2
Summary: X.org null input driver
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-void xorg/drivers/xf86-input-void
# cd xorg/drivers/xf86-input/void
# git-archive --format=tar --prefix=xf86-input-void-1.1.1/ xf86-input-void-1.1.1 | bzip2 -9 > xf86-input-void-1.1.1.tar.bz2
########################################################################
Source0: xf86-input-void-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-void-1.1.1..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
Void is a dummy/null X.org input driver.
It doesn't connect to any physical device, and it never delivers any events.
It functions as both a pointer and keyboard device, and may be used as X
server's core pointer and/or core keyboard.
It's purpose is to allow the X server to operate without a core pointer
and/or core keyboard.

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-input-void-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# Create list of dependencies
x-check-deps.pl
for deps in *.deps; do
    install -D -m 644 $deps %{buildroot}/%{_datadir}/X11/mandriva/$deps
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/void_drv.so
%{_mandir}/man4/void.*

%files devel
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/*.la
%{_datadir}/X11/mandriva/*.deps
