%include        /usr/lib/rpm/macros.perl
Summary:	EpgDownloader is a written in perl, plugin based programme guide converter
Name:		epgdownloader
Version:	0.7.2
Release:	0.3
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/epgdownloader/%{name}-%{version}.tgz
# Source0-md5:	8aeff68a55fb659422fc2cdf53fef144
URL:		http://epgdownloader.sourceforge.net
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(include::.*)' 'perl(plugins::.*)' 'perl(paths)'

%define         _sysconfdir	/etc/%{name}
%define         _pkglibdir	/usr/share/%{name}

%description
EpgDownloader is a written in perl, plugin based programme guide
converter. With derivered plugins you can for example download tv
schedule from website and export it to xmltv or VDR's epg.data format

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT{%_pkglibdir/{include,plugins},%_sysconfdir}

install channels.xml $RPM_BUILD_ROOT%_sysconfdir
install config.xml $RPM_BUILD_ROOT%_sysconfdir

ln -s %_sysconfdir/config.xml $RPM_BUILD_ROOT%_pkglibdir/
ln -s %_sysconfdir/channels.xml $RPM_BUILD_ROOT%_pkglibdir/

install epgdownloader.pl $RPM_BUILD_ROOT%_pkglibdir
install run.sh $RPM_BUILD_ROOT%_pkglibdir
install paths.pm $RPM_BUILD_ROOT%_pkglibdir

cp -a plugins $RPM_BUILD_ROOT%_pkglibdir
cp -a include $RPM_BUILD_ROOT%_pkglibdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%_pkglibdir/channels.xml
%_pkglibdir/config.xml
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/channels.xml
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/config.xml
%dir %_pkglibdir
%dir %_sysconfdir
%dir %_pkglibdir/include
%_pkglibdir/include/*.pm
%_pkglibdir/paths.pm
%attr(755,root,root) %_pkglibdir/epgdownloader.pl
%attr(755,root,root) %_pkglibdir/run.sh
%_pkglibdir/plugins

%doc ChangeLog NEWS README TODO
