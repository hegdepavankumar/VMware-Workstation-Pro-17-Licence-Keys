
## Downloading and installing VMware Workstation 

## Purpose

The article provides steps to download and install VMware Workstation.

Before downloading and installing VMware Workstation:

Ensure that your physical machine meets the system requirements for VMware Workstation. For more information, see System Requirements:

1. Workstation CPU Requirements

This article lists the CPU requirements for running VMware Workstation Pro/Workstation Player 14.x , 15.x and 16.x. or latest

Resolution
* Systems using Processors (CPUs) launched in 2011 or later are supported except:
* Intel Atom processors based on the 2011 “Bonnell” micro-architecture (e.g. Atom Z670/Z650; Atom N570)
* Systems using Intel Atom processors based on the 2012 “Saltwell” micro-architecture (e.g. Atom S1200, Atom D2700/D2500, Atom N2800/N2600.
* Systems using AMD processors based on the “Llano” and “Bobcat” micro-architectures (e.g. code-named “Hondo”, “Ontario”, “Zacate”, “Llano”)

In addition, the following are supported:

Systems using Intel processors based on the 2010 “Westmere” micro-architecture (e.g. Xeon 5600, Xeon 3600, Core i7-970, Core i7-980, Core i7-990)

2. Workstation Host OS Support:

[Click here to read](https://kb.vmware.com/s/article/80807)



## Downloading VMware Workstation

* To download VMware Workstation:
* Navigate to the VMware Workstation Download Center.
* Based on your requirements, click Go to Downloads for VMware Workstation for Windows or VMware Workstation for Linux.
* Click Download Now.
* If prompted, log in to your Customer Connect profile. If you do not have a profile, create one. For more information, see How to create a Customer Connect profile (2007005).
* Ensure that your profile is complete and enter all mandatory fields. For more information, see How to update your Customer Connect profile (2086266).
* Review the End User License Agreement and click Yes.
* Click Download Now.

If the installer fails to download during the download process:
Delete the cache in your web browser. For more information, see:
 
* Mozilla Firefox: How to clear the Firefox cache- [read](https://support.mozilla.org/en-US/kb/how-clear-firefox-cache)
* Google Chrome: Delete your cache and other browser data - [read](https://support.google.com/chrome/answer/2392709?hl=en&visit_id=638341485894904371-212168826&rd=1)
* Microsoft Internet Explorer: How to delete the contents of the Temporary Internet Files folder- [read](https://support.microsoft.com/en-us/topic/how-to-delete-the-contents-of-the-temporary-internet-files-folder-8eb83a8d-43e2-300d-d355-2ee71602ab44)
* Disable the pop-up blocker in your web browser. For more information, see:
 
    * Mozilla Firefox: How do I disable a Pop-up blocker?- [read](https://support.mozilla.org/en-US/questions/714476)
    * Google Chrome: Manage pop-ups.- [read](https://support.google.com/chrome/answer/95472?hl=en)
    * Microsoft Internet Explorer: How to turn Internet Explorer Pop-up Blocker on or off on a Windows XP SP2-based computer.- [read](https://support.microsoft.com/en-us/windows/change-security-and-privacy-settings-for-internet-explorer-11-9528b011-664c-b771-d757-43a2b78b2afe)

- Download using a different web browser application.
- Disable any local firewall software.
- Restart the virtual machine.
- Download the installer from a different computer or network.

### Installing VMware Workstation

Notes:

  - You must have only one VMware Workstation installed at a time. You must uninstall the previous version of VMware Workstation before installing a new version.
  - If the installer reports an error when you run it, you must verify the download. For more information, see Verifying the integrity of downloaded installer files (1537).
  

### To install VMware Workstation on a Windows host:
  
  1. Log in to the Windows host system as the Administrator user or as a user who is a member of the local Administrators group.
  2. Open the folder where the VMware Workstation installer was downloaded. The default location is the Downloads folder for the user account on the Windows host.

  Note: The installer file name is similar to VMware-workstation-full-xxxx-xxxx.exe, where xxxx-xxxx is the version and build numbers.
 
  3. Right-click the installer and click Run as Administrator.
  4. Select a setup option:

       - Typical: Installs typical Workstation features. If the Integrated Virtual Debugger for Visual Studio or Eclipse is present on the host system, the associated Workstation plug-ins are installed.
       - Custom: This lets you select which Workstation features to install and specify where to install them. Select this option if you need to change the shared virtual machines directory, modify the VMware Workstation Server port, or install the enhanced virtual keyboard driver. The enhanced virtual keyboard driver provides better handling of international keyboards and keyboards that have extra keys.
 
  5. Follow the on-screen instructions to finish the installation.
  6. Restart the host machine.


### To install VMware Workstation on a Linux host:

Note: VMware Workstation for Linux is available as a .bundle download in the VMware Download Center. The Linux bundle installer starts a GUI wizard on most Linux distributions. In some Linux distributions, the bundle installer starts a command-line wizard instead of a GUI wizard.

1. Log in to the Linux host with the user account that you plan to use with VMware Workstation.
2. Open a terminal interface. For more information, see Opening a command or shell prompt (1003892).
3. Change to root. For example:

```su root```

 - Note: The command that you use depends on your Linux distribution and configuration.
 
4. Change directories to the directory that contains the VMware Workstation bundle installer file. The default location is the Download directory.
5. Run the appropriate Workstation installer file for the host system.
```
For example:

sh VMware-workstation-Full-xxxx-xxxx.architecture.bundle [--option]
```
  Where:
      - xxxx-xxxx is the version and build numbers
      - architecture is i386 or x86_64
      - option is a command line option


This table describes the command line options:

| Option | Description |
|----------|----------|
| --gtk | Opens the GUI-based VMware installer, which is the default option. |
| --console | Use the terminal for installation. |
| --custom | 	Use this option to customize the locations of the installation directories and set the hard limit for the number of open file descriptors. |
| --regular | 	Shows installation questions that have not been answered before or are required. This is the default option. |
| --ignore- or -I | Allows the installation to continue even if there is an error in one of the installer scripts. Because the section that has an error does not complete, the component might not be properly configured. |
| --required | Shows the license agreement only and then proceeds to install Workstation |



 

6. Accept the license agreement.

  Note: If you are using the --console option or installing VMware Workstation on a Linux host that does not support the GUI wizard, press Enter to scroll through and read the license agreement or type q to skip to the yes/no prompt.
 
7. Follow the on-screen instructions or prompts to finish the installation.
8. Restart the Linux host.


### After installation

On Windows host systems:

  - The installer creates a desktop shortcut, a quick launch shortcut, or a combination of these options in addition to a Start Menu item.
  - To start VMware Workstation on a Windows host system, select Start > Programs > VMware Workstation.

On Linux host systems:

  - VMware Workstation can be started from the command line on all Linux distributions.
  - On some Linux distributions, VMware Workstation can be started in the GUI from the System Tools menu under Applications.
  - To start VMware Workstation on a Linux host system from the command line, run the vmware & command in a terminal window. For more information, see Opening a command or shell prompt (1003892).

For example:
```
/usr/bin/vmware &
```

When you start the Workstation for the first time, Workstation prompts you to accept the End User License Agreement. After you start the Workstation, the Workstation window opens.
