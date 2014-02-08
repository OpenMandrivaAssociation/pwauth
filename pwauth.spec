Summary:	A Unix Web Authenticator
Name:		pwauth
Version:	2.3.9
Release:	5
License:	BSD
Group:		System/Servers
URL:		http://code.google.com/p/pwauth/
Source0:	http://pwauth.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	pwauth.pam
Patch0:		pwauth-typo_fix.diff
Patch1:		pwauth-config.diff
Patch2:		pwauth-2.3.2-pam.diff
Patch3:		pwauth-2.3.2-server.diff
Patch4:		pwauth-ldflags_fix.diff
BuildRequires:	pam-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Pwauth is an authenticator designed to be used with
mod_auth_external and the Apache HTTP Daemon to support reasonably
secure web authentication out of the system password database on
most versions of Unix. 

What pwauth actually does is very simple. Given a login and a
password, it returns a status code indicating whether it is a
valid login/password or not. It is normally installed as an
suid-root program, so other programs (like Apache or a CGI
program) can run it to check if a login/password is valid even
though they don't themselves have read access to the system
password database.

%prep

%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

cp %{SOURCE1} pwauth.pam

%build
%serverbuild

%make CFLAGS="$CFLAGS" LDFLAGS="%{ldflags}" LIB="-lpam -ldl"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/pam.d
install -d %{buildroot}%{_bindir}

install -m0755 pwauth %{buildroot}%{_bindir}/
install -m0755 unixgroup %{buildroot}%{_bindir}/

install -m0644 pwauth.pam %{buildroot}%{_sysconfdir}/pam.d/pwauth
install -m0644 pwauth.pam %{buildroot}%{_sysconfdir}/pam.d/unixgroup

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES FORM_AUTH INSTALL README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/pwauth
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/unixgroup
%attr(04550,root,apache) %{_bindir}/pwauth
%attr(04550,root,apache) %{_bindir}/unixgroup


%changelog
* Mon May 30 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.9-1mdv2011.0
+ Revision: 681820
- 2.3.9

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.8-4
+ Revision: 667899
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.8-3mdv2011.0
+ Revision: 607248
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.8-2mdv2010.1
+ Revision: 519062
- rebuild

* Sun Jun 21 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3.8-1mdv2010.0
+ Revision: 387621
- 2.3.8
- new url
- rediffed patches

* Wed Mar 11 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3.7-1mdv2009.1
+ Revision: 353771
- 2.3.7

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3.6-2mdv2009.1
+ Revision: 317558
- rebuild

* Sun Aug 03 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3.6-1mdv2009.0
+ Revision: 262179
- 2.3.6
- rediffed P1
- fixed a typo (P0)
- set ldflags (P4)
- use %%serverbuild macro

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.3.2-4mdv2009.0
+ Revision: 225118
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-3mdv2008.1
+ Revision: 179371
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-2mdv2007.0
+ Revision: 134448
- Import pwauth

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-2
- bunzip sources

* Sat Feb 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-1mdk
- 2.3.2
- drop P0, seems implemented upstream
- rediffed patches; P1,P2,P3

* Sat Feb 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.8-4mdk
- use "include" directive instead of deprecated pam_stack module

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.2.8-3mdk
- Rebuild

* Tue May 03 2005 Luca Berra <bluca@vodka.it> 2.2.8-2mdk
- disable the SERVER_UID feature, apache userid is dynamic

* Mon Feb 14 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.8-1mdk
- initial Mandrakelinux package

