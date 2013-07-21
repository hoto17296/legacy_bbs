#!/usr/bin/perl

use DateTime;

# 設定色々
my $log_file = "log.dat";

my $layout_dir = "layout/";
my $asset_dir  = "assets/";
my $icon_dir   = $asset_dir . "icons/";

my $default_icon = "anonymous.gif";

my $header_file = $layout_dir . "header.html";
my $footer_file = $layout_dir . "footer.html";
my $post_file   = $layout_dir . "post.html";

# ヘッダーを表示
print &load_file($header_file);

# 投稿を表示
my $format = &load_file($post_file);
open(my $fp, "<", $log_file) or die "Cannot open $file: $!";
while(my $post = readline $fp){
  chomp $post;
  my ($time,$name,$value,$icon) = split(/\t+/, $post);
  my $dt = DateTime->from_epoch( time_zone => 'Asia/Tokyo', epoch => $time );
  $icon = $default_icon unless ($icon);
  printf($format, $icon_dir.$icon, $name, $value, $dt->strftime("%H:%M"));
}
close $fp;

# フッターを表示
print &load_file($footer_file);


sub load_file {
  $file = $_[0];
  open(IN, "< $file");
  read (IN, $buffer, (-s $file));
  close IN;
  return $buffer;
}
