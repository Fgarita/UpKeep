; Inno Setup script for PC Maintenance.
;
; 1. Install Inno Setup (free): https://jrsoftware.org/isdl.php
; 2. Build the app first: build.bat  (creates dist\PC Maintenance\)
; 3. Compile this script: iscc installer.iss
;    (or open it in the Inno Setup Compiler and click Build)
;
; The result is Output\PC-Maintenance-Setup.exe — a normal Windows
; installer your users double-click, with a Start Menu shortcut, an
; optional Desktop shortcut, and an uninstaller.

#define MyAppName "PC Maintenance"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Your Name"
#define MyAppExeName "PC Maintenance.exe"

[Setup]
AppId={{8F1B7C2E-3A4D-4E6F-9B2A-PCMAINTENANCE1}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
OutputDir=Output
OutputBaseFilename=PC-Maintenance-Setup
SetupIconFile=assets\app.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
; The app itself requests admin (UAC) on launch, so the installer
; doesn't need elevated rights just to copy files for the current user.
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\PC Maintenance\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#MyAppName}}"; Flags: nowait postinstall skipifsilent
