Summary:	DevHelp book: libgnome
Summary(pl):	Ksi±¿ka do DevHelp'a o libgnome
Name:		devhelp-book-libgnome
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libgnome.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about libgnome

%description -l pl
Ksi±¿ka do DevHelp o libgnome

%prep
%setup -q -c libgnome -n libgnome

%build
mv -f book libgnome
mv -f book.devhelp libgnome.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/libgnome
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install libgnome.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install libgnome/* $RPM_BUILD_ROOT%{_prefix}/books/libgnome

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
