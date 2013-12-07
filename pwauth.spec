Summary:	A Unix Web Authenticator
Name:		pwauth
Version:	2.3.9
Release:	7
License:	BSD
Group:		System/Servers
Url:		http://code.google.com/p/pwauth/
Source0:	http://pwauth.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	pwauth.pam
Patch0:		pwauth-typo_fix.diff
Patch1:		pwauth-config.diff
Patch2:		pwauth-2.3.2-pam.diff
Patch3:		pwauth-2.3.2-server.diff
Patch4:		pwauth-ldflags_fix.diff
BuildRequires:	pam-devel

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
install -d %{buildroot}%{_sysconfdir}/pam.d
install -d %{buildroot}%{_bindir}

install -m0755 pwauth %{buildroot}%{_bindir}/
install -m0755 unixgroup %{buildroot}%{_bindir}/

install -m0644 pwauth.pam %{buildroot}%{_sysconfdir}/pam.d/pwauth
install -m0644 pwauth.pam %{buildroot}%{_sysconfdir}/pam.d/unixgroup

%files
%doc CHANGES FORM_AUTH INSTALL README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/pwauth
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/unixgroup
%attr(04550,root,apache) %{_bindir}/pwauth
%attr(04550,root,apache) %{_bindir}/unixgroup

