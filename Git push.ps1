# Set the path to your Git repository
$repoPath = "C:\Users\jakko\Desktop\Kool\Jakko_leht"

# Set the commit message
$commitMessage = "Automated commit - $(Get-Date)"

# Change directory to the Git repository
cd $repoPath

# Add all changes
git add .

# Commit changes with the specified message
git commit -m $commitMessage

# Push changes to the remote repository (assuming origin and main branch, change accordingly)
git push
