%include	/usr/lib/rpm/macros.perl
%define		pdir	BSD
%define		pnam	Resource
Summary:	Perl module with BSD process resource limit functions
Summary(pl):	Modu³ Perla z funkcjami BSD obs³uguj±cymi limity zasobów dla procesów
Name:		perl-BSD-Resource
Version:	1.22
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl extension implements the BSD process resource limit
functions (getrusage(), getrlimit(), setrlimit()) and the BSD process
priority functions. These are available also via core Perl but here we
do more tricks so that the PRIO_* are available (getpriority(),
setpriority()).

%description -l pl
To rozszerzenie Perle jest implementacj± funkcji BSD dotycz±cych
limitów zasobów dla procesów (getrusage(), getrlimit(), setrlimit())
oraz funkcji BSD zwi±zanych z priorytetami procesów. S± one dostêpne
tak¿e z podstawowego Perla, ale ten modu³ pozwala na wiêcej sztuczek,
bo dostêpne s± PRIO_* (getpriority(), setpriority()).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitearch}/BSD/Resource.pm
%dir %{perl_sitearch}/auto/BSD/Resource
%{perl_sitearch}/auto/BSD/Resource/*.al
%{perl_sitearch}/auto/BSD/Resource/autosplit.ix
%{perl_sitearch}/auto/BSD/Resource/Resource.bs
%attr(755,root,root) %{perl_sitearch}/auto/BSD/Resource/Resource.so
%{_mandir}/man3/*
