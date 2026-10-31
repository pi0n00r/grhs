param(
    [string]$Source = (Join-Path (Split-Path -Parent $PSScriptRoot) 'GRHS-v0.4.0.docx'),
    [string]$Destination = (Join-Path (Split-Path -Parent $PSScriptRoot) 'GRHS-v0.4.0.pdf')
)

$ErrorActionPreference = 'Stop'
$sourcePath = (Resolve-Path -LiteralPath $Source).Path
$destinationPath = [System.IO.Path]::GetFullPath($Destination)

$word = $null
$document = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $document = $word.Documents.Open($sourcePath, $false, $false)
    $document.Fields.Update() | Out-Null
    foreach ($toc in $document.TablesOfContents) {
        $toc.Update() | Out-Null
    }
    $document.Save()
    $wdExportFormatPDF = 17
    $document.ExportAsFixedFormat($destinationPath, $wdExportFormatPDF)
    Write-Output "WROTE $destinationPath"
}
finally {
    if ($null -ne $document) {
        $document.Close($false)
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($document)
    }
    if ($null -ne $word) {
        $word.Quit()
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

