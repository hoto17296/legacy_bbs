#!/usr/local/bin/perl

%directors = (
  '宮崎駿'   => 71,
  '庵野秀明' => 52,
  '今敏'     => 46,
  '新海誠'   => 39,
  '大友克洋' => 58,
  '押井守'   => 45,
  '細田守'   => 45,
  '原恵一'   => 59
);

foreach $name ( keys %directors ){
  $total += $directors{$name};
  $number++;
}
$average = $total / $number;

print "Total: $total\n";
print "Number: $number\n";
print "Average: $average\n";
