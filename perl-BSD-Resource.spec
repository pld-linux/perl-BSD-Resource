%include	/usr/lib/rpm/macros.perl
Summary:	BSD-Resource perl module
Summary(pl):	Modu³ perla BSD-Resource
Name:		perl-BSD-Resource
Version:	1.0701
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/BSD/BSD-Resource-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BSD-Resource - BSD process resource limit and priority functions.

%description -l pl
BSD-Resource - modu³ zawiera rozszerzon± implementacjê funkcji ograniczenia
zasobów procesów i pierwszeñstwa procesów.

%prep
%setup -q -n BSD-Resource-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded \
	$RPM_BUILD_ROOT/%{perl_sitearch}/auto/BSD/Resource/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/BSD/Resource
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitearch}/BSD/Resource.pm

%dir %{perl_sitearch}/auto/BSD/Resource
%{perl_sitearch}/auto/BSD/Resource/.packlist
%{perl_sitearch}/auto/BSD/Resource/*.al
%{perl_sitearch}/auto/BSD/Resource/autosplit.ix
%{perl_sitearch}/auto/BSD/Resource/Resource.bs
%attr(755,root,root) %{perl_sitearch}/auto/BSD/Resource/Resource.so

%{_mandir}/man3/*
