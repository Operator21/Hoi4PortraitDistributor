#!/usr/bin/env fish
# get path to hearts of iron from parameter
set gamePath $1
set portraits ""

echo "Getting portrait directories:"
for dir in (find $gamePath -type d -name leaders)
	echo "	$dir"
	for file in (find $dir -type f -name "*.dds")
		set -a portraits "
$file"
	end   
end

echo $portraits > "all_list.txt"