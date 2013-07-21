#!/usr/bin/perl

use Data::Dumper;
use DateTime;
use CGI;

# 設定色々

our $log_file = "log.dat";

my $layout_dir = "layout/";
my $asset_dir  = "assets/";
my $icon_dir   = $asset_dir . "icons/";

my $default_icon = "anonymous.gif";

my $header_file = $layout_dir . "header.html";
my $footer_file = $layout_dir . "footer.html";
my $post_file   = $layout_dir . "post.html";

# 投稿
&insert_post() if ($ENV{'REQUEST_METHOD'} eq 'POST');

# ヘッダーを表示
print &load_file($header_file);

# 投稿を表示
our $post_format = &load_file($post_file);
open(FP, "<", $log_file) or die "Cannot open $file: $!";
while(my $post = readline FP){
  &show_post($post);
}
close FP;

# フッターを表示
print &load_file($footer_file);

sub load_file {
  $file = $_[0];
  open(FP, "<", $file);
  read (FP, $buffer, (-s $file));
  close FP;
  return $buffer;
}

sub show_post {
  chomp $_[0];
  my ($time,$name,$value,$icon) = split(/\t+/, $_[0]);
  my $dt = DateTime->from_epoch( time_zone => 'Asia/Tokyo', epoch => $time );
  $icon = $default_icon unless ($icon);
  printf($post_format, $icon_dir.$icon, $name, $value, $dt->strftime("%H:%M"));
}

sub insert_post {
  my $cgi = new CGI;
  %post = (
    'time'  => time(),
    #'name'  => $cgi->param('name'),
    'name'  => '名無しさん',
    'value' => &sanitize($cgi->param('value')),
    'icon'  => &sanitize($cgi->param('icon'))
  );
  if (&validation(%post)){
    open(FP, ">>", $log_file) or die("error :$!");
    flock(FP, LOCK_EX);
    print FP "$post{'time'}\t$post{'name'}\t$post{'value'}\t$post{'icon'}\n";
    close FP;
  }
  print $cgi->redirect('bbs.cgi');
}

sub validation {
  %post = @_;
  if ($post{'value'}){
    return 1;
  }
  else {
    return 0;
  }
}

sub sanitize {
  $str = $_[0];
  my %table = (
    '&'    => '&amp;',
    '<'    => '&lt;',
    '>'    => '&gt;',
    '"'    => '&quot;',
    "'"    => '&#39;',
    "\r\n" => '<br/>',
    "\n"   => '<br/>',
    "\r"   => '<br/>',
    "\t"   => ' '
  );
  my $regex = join '', '([', keys(%table), '])';
  $str =~ s/$regex/$table{$1}/go;
  return $str;
}
