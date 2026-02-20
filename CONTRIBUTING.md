# Contributing to Taskboard

Thanks for taking the time to look at this project! Here's how to get involved.

## Reporting bugs

If you find something broken, open an issue and include:

- What you did (steps to reproduce)
- What you expected to happen
- What actually happened
- Your Python version and OS if it seems relevant

Please check the existing issues first to avoid duplicates.

## Fixing bugs / making changes

1. Fork the repo
2. Create a branch — name it something like `fix/delete-bug` or `feature/add-login`
3. Make your changes
4. Test that nothing else broke
5. Open a pull request with a clear description of what you changed and why

**When submitting a PR that fixes a bug, reference the issue number in your PR description or commit message** using `Fixes #<issue-number>` or `Closes #<issue-number>`. This links the PR to the issue and automatically closes it when the PR is merged.

For example:
```
Fix delete route removing wrong tasks

The list comprehension had the condition backwards, so deleting a task
would remove everything except the selected task.

Fixes #4
```

## Code style

Nothing strict — just try to keep it consistent with the existing code. Comments are welcome if something isn't obvious.

## Questions?

Open an issue and tag it with the `question` label. 
