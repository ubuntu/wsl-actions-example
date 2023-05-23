# Example usage of WSL Github actions

Over at the [Ubuntu/WSL](https://github.com/ubuntu/WSL) repository, we developed some GitHub actions to
make your life easier when running your CI in WSL. This is needed because GitHub runners do not support
WSL. Just setting up an Azure VM will not cut it either, because the runner will run in session 0, which means
that Microsoft Store applications such as WSL cannot be run.

## How to run your CI on WSL
1. Set up a Windows machine to run your CI in. GitHub runners won't do the job, but Azure VMs will.
2. Set up an auto-logon in your Windows machine. See [here](https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon) for a step-by-step guide.
3. Add the GitHub runner as a startup application (specifically, the `run.cmd` batch file in your actions runner).

You're done! Your CI yaml files will need some extra work, however, as you need to allocate and deallocate the VM on demand.
The runner needs to run on Windows and not directly on WSL, as WSL instances will shut themselves down automatically, so we implemented some utilities to
install and update WSL and the distro, as well as to run scripts.

You can find these actions [here](github.com/Ubuntu/WSL/.github/actions).

## What is this repo?
This repository contains a very simple library `src.py` with a function that returns different results inside and outside WSL.
To test it properly, we run a test on each platform:
- Ubuntu in a GitHub Runner: ./.github/workflows/test.yaml
- Ubuntu in WSL: ./.github/workflows/test_wsl.yaml
