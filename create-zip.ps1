$ScriptPath = Split-Path $MyInvocation.MyCommand.Path -Parent
$FolderName = "$($ScriptPath)/output/plugin.audio.tuneinradio/"

if (Test-Path $FolderName) {
   
    Write-Host "Folder Exists... deleting"
    # Perform Delete folder operation
    Remove-Item $FolderName -Recurse
}

Write-Host "Folder Doesn't Exists... creating"
# Create directory if not exists
New-Item $FolderName -ItemType Directory

Write-Host "Copying content..."
# Copy the content of the folder to the output
Copy-Item -Path "$($ScriptPath)/resources" -Destination $FolderName -Recurse
Copy-Item -Path "$($ScriptPath)/addon.py" -Destination $FolderName
Copy-Item -Path "$($ScriptPath)/addon.xml" -Destination $FolderName
Copy-Item -Path "$($ScriptPath)/changelog.txt" -Destination $FolderName
Copy-Item -Path "$($ScriptPath)/LICENSE" -Destination $FolderName
Copy-Item -Path "$($ScriptPath)/README.md" -Destination $FolderName

Write-Host "Creating zip file..."
# Creates a zip file
Compress-Archive -Path $FolderName -DestinationPath "$($ScriptPath)/output/plugin.audio.tuneinradio.zip"