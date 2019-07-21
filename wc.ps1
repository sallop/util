<#
  wc - alternative command 
#>
Get-Content $args[0] | Measure-Object -Line
