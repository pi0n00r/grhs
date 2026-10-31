param(
    [string]$Source = (Join-Path (Split-Path -Parent $PSScriptRoot) 'build\GRHS-v0.4.0.docx'),
    [string]$Destination = (Join-Path (Split-Path -Parent $PSScriptRoot) 'build\GRHS-v0.4.0.pdf')
)

$ErrorActionPreference = 'Stop'
$sourcePath = (Resolve-Path -LiteralPath $Source).Path
$destinationPath = [System.IO.Path]::GetFullPath($Destination)
$destinationDirectory = Split-Path -Parent $destinationPath
[System.IO.Directory]::CreateDirectory($destinationDirectory) | Out-Null
$temporarySource = Join-Path ([System.IO.Path]::GetTempPath()) ("GRHS-{0}.docx" -f [guid]::NewGuid().ToString('N'))
Copy-Item -LiteralPath $sourcePath -Destination $temporarySource

$word = $null
$document = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $document = $word.Documents.Open($temporarySource, $false, $false)
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
    if (Test-Path -LiteralPath $temporarySource) {
        Remove-Item -LiteralPath $temporarySource -Force
    }
}

