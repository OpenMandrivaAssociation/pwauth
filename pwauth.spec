Summary:	A Unix Web Authenticator
Name:		pwauth
Version:	2.3.2
Release:	%mkrel 2
License:	BSD
Group:		System/Servers
URL:		http://www.unixpapa.com/pwauth/
Source0:	http://www.unixpapa.com/software/%{name}-%{version}.tar.bz2
Source1:	pwauth.pam
Patch1:		pwauth-2.3.2-config.diff
Patch2:		pwauth-2.3.2-pam.diff
Patch3:		pwauth-2.3.2-server.diff
BuildRequires:	pam-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
%patch1 -p0
%patch2 -p0
%patch3 -p1

cp %{SOURCE1} pwauth.pam

%build

%make CFLAGS="%{optflags}" LIB="-lpam -ldl"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/pam.d
install -d %{buildroot}%{_bindir}

install -m0755 pwauth %{buildroot}%{_bindir}/
install -m0755 unixgroup %{buildroot}%{_bindir}/

install -m0644 pwauth.pam %{buildroot}%{_sysconfdir}/pam.d/pwauth
install -m0644 pwauth.pam %{buildroot}%{_sysconfdir}/pam.d/unixgroup

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES FORM_AUTH INSTALL README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/pwauth
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/unixgroup
%attr(04550,root,apache) %{_bindir}/pwauth
%attr(04550,root,apache) %{_bindir}/unixgroup


