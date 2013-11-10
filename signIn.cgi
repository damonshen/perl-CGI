#!/usr/bin/perl -w
use CGI;
use DBI;
my $cgi = new CGI;
my $account = $cgi->param('account');
my $password = $cgi->param('password');

$DB_user = 'root';
$DB_pwd = 'supreme';
$DB_name = 'wp_server';

$dbh = DBI->connect("dbi:mysql:database=$DB_name;",$DB_user,$DB_pwd) or die "Connect Error";
$SQL= "select password,name from user where account = '$account'";
$selectRecord = $dbh->prepare($SQL);
$selectRecord->execute();
$ref = $selectRecord->fetchrow_hashref();

#print "Content-type: text/html\n\n"; # HTTP header
#print $cgi->header("text/html");
if ($ref && $ref->{'password'} eq $password) {
	my $cookie = $cgi->cookie( -name=>'name',
			-value=>"$ref->{'name'}",
			-expires=>'+1h',
			-domain=>'',
			-path=>'/',
			);
	print $cgi->header( -cookie=>$cookie);
	print "success";
} else {
	print "wrong account or password";;
#print "Failure<br/>$DBI::errstr";
}

$dbh->disconnect();
