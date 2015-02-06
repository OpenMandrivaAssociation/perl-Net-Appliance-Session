%define upstream_name Net-Appliance-Session
%define upstream_version 4.131260

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Net::Appliance::Phrasebook\\)'
%endif

Summary:	Run command-line sessions to network appliances
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Net-Appliance-Session/
Source:		http://www.cpan.org/modules/by-module/Net/Net-Appliance-Session-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Run command-line sessions to network appliances

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%files
%doc Changes  MANIFEST META.yml README examples/
%{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Net/Appliance/Session
%{perl_vendorlib}/Net/Appliance/Session.pm
%{_bindir}/nas
%{_mandir}/man1/nas.1.xz

%changelog
* Tue Sep 27 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.36-1mdv2012.0
+ Revision: 701541
- first mandriva version
- Created package structure for 'perl-Net-Appliance-Session'.


