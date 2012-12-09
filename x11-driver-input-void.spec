Name: x11-driver-input-void
Version: 1.4.0
Release: 4
Summary: X.org null input driver
Group: System/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-void-%{version}.tar.bz2
License: MIT
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Void is a dummy/null X.org input driver.
It doesn't connect to any physical device, and it never delivers any events.
It functions as both a pointer and keyboard device, and may be used as X
server's core pointer and/or core keyboard.
It's purpose is to allow the X server to operate without a core pointer
and/or core keyboard.

%prep
%setup -q -n xf86-input-void-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/void_drv.so
%{_mandir}/man4/void.*


%changelog
* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.4.0-1mdv2011.0
+ Revision: 683669
- New version 1.4.0.
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3
+ Revision: 671134
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.1-2mdv2011.0
+ Revision: 595750
- require xorg server with proper ABI

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.3.1-1mdv2011.0
+ Revision: 591823
- new release

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.0-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3.0-1mdv2010.1
+ Revision: 464263
- New version: 1.3.0

* Thu Feb 26 2009 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2009.1
+ Revision: 345051
- new release
- fix group

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-5mdv2009.0
+ Revision: 225950
- rebuild

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-4mdv2008.1
+ Revision: 160499
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-3mdv2008.1
+ Revision: 156594
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-2mdv2008.1
+ Revision: 154898
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Another easy one. There is already a tag named xf86-input-void-1.1.1, and
  it matches git master at the time of creation of the mandriva branch, so,
  just updating spec documentation.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-1mdv2008.1
+ Revision: 97068
- new upstream version: 1.1.1
- minor spec cleanup

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2008.0
+ Revision: 75714
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:03:02 (31708)
- fill in summary & descriptions for all input drivers

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 19:59:30 (31594)
- Updated drivers for X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

