# listOfEntries.ps1 - Retrieve the keys for the new entries in the
# bibliography.

$message = "Add "; 

# Accumulate the list of entries
git --no-pager diff .\bibliography.bib | 
Select-String -pattern "[+]@" | 
Foreach-Object { 
    $message += $_ -Replace '^[^{]*[{]', ''; 
    $message += ' '; 
}

$message = $message -Replace ', (\S+),\s*$', ', and $1'

Write-Output $message