<#
-Delimiter
-Encoding
-Header
-LiteralPath
-Path
-UseCulture

#get-content -path $file
#$p | get-member

#>

$filepath = "remove-m.csv"
#$csv = import-csv -path $path
#
##$csv | %{
##  write-host $_
##}
#
#function Get-CsvColumnIndex {
#  param ($column, $array)
#  $cols = Get-CsvColumns $array
#  $cindex = [array]::IndexOf($cols,"$column")
#  return $cindex
#}

<#
select-object
-First -Last -Unique
#>

#$content = get-content $filepath
$content = import-csv $filepath

$header = $content | select-object -first 1

#$header = $header.split(",")
write-host $header

# $content | % {
foreach ($line in $content){
  write-host $_.policyID
}

# $body = $content | select-object 
