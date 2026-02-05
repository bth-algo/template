# Workflow Automation Guide

This document describes the automated workflow commands available for students working through assignments.

## Quick Start

```bash
# Initial setup (run once)
uv run task setup

# Start your first assignment
uv run task start-kmom -- kmom01

# Develop and test
uv run tester tests/kmom01
uv run ruff check src/kmom01

# Check readiness and submit
uv run task check-ready -- kmom01
```

## Available Commands

### 🚀 Getting Started

#### `task setup`
Runs complete initial setup:
- Creates source directory structure
- Downloads test files
- Downloads configuration files (ruff.toml, workflows, extensions)
- Validates all required files exist

```bash
uv run task setup
```

#### `task help`
Shows comprehensive help with all available commands organized by category.

```bash
uv run task help
```

#### `task status`
Shows current assignment status including:
- Current branch
- Source directory contents
- Uncommitted changes
- Available assignment branches
- Next steps

```bash
uv run task status
```

---

### 📝 Testing Commands

#### `task test`
Run tests for a specific assignment or all tests.

```bash
# Test specific assignment
uv run task test -- kmom01

# Test all assignments
uv run task test
```

#### `task test-struct`
Run only structure tests (validates file/function existence).

```bash
uv run task test-struct -- kmom01
```

#### `task test-extra`
Run only extra credit tests.

```bash
uv run task test-extra -- kmom01
```

#### `task test-tag`
Run tests with a specific tag (uses pytest markers).

```bash
uv run task test-tag -- kmom01 tag_name
```

#### `task test-quick`
Run tests without verbose output (faster).

```bash
uv run task test-quick -- kmom01
```

---

### 🧹 Code Quality Commands

#### `task lint`
Check code with Ruff linter (no changes made).

```bash
uv run task lint
```

#### `task lint-all`
Check all Python files including tests.

```bash
uv run task lint-all
```

#### `task format-check`
Check if code formatting is correct (no changes made).

```bash
uv run task format-check
```

#### `task format`
Format code with Ruff (WARNING: modifies files).

```bash
uv run task format
```

---

### 🔀 Branch Management Commands

#### `task start-kmom`
Create and checkout a new assignment branch. Automatically determines source branch:
- `kmom01` branches from `main`
- `kmom02` branches from `kmom01`
- `kmom03` branches from `kmom02`
- etc.

```bash
uv run task start-kmom -- kmom02
```

If branch already exists, switches to it instead of creating.

#### `task switch-kmom`
Switch to an existing assignment branch.

```bash
uv run task switch-kmom -- kmom01
```

#### `task branches`
List all assignment branches and show current branch.

```bash
uv run task branches
```

---

### ✅ Submission Commands

#### `task check-ready`
Comprehensive readiness check that verifies:
- On correct branch
- No uncommitted changes
- Structure tests pass
- All tests pass
- Ruff linting passes

```bash
uv run task check-ready -- kmom01
```

Exit code 0 = ready to submit, non-zero = issues found.

#### `task tag-version`
Create a version tag for assignment following the format `v{kmom_number}.{version}`.

```bash
# Create tag v1.1.0.0 for kmom01
uv run task tag-version -- kmom01 1.0.0

# Create tag v2.1.0 for kmom02
uv run task tag-version -- kmom02 1.0
```

Push tags with: `git push origin v1.1.0`

---

### 📥 Update Commands

These are the original commands for downloading/updating files:

#### `task download-tests`
Update test files from artifact repository.

```bash
uv run task download-tests
```

#### `task download-ruff-config`
Update Ruff configuration.

```bash
uv run task download-ruff-config
```

#### `task download-workflow`
Update GitHub Actions workflow.

```bash
uv run task download-workflow
```

#### `task download-extensions`
Update VS Code recommended extensions.

```bash
uv run task download-extensions
```

#### `task download-lab`
Download lab exercises (must be run from within lab directory).

```bash
cd src/kmom01/lab_01
uv run task download-lab -- lab_01
```

#### `task check-have-files`
Verify all required files exist.

```bash
uv run task check-have-files
```

---

## Typical Workflow Example

### Starting Assignment 1

```bash
# 1. Initial setup (first time only)
uv run task setup

# 2. Create branch for kmom01
uv run task start-kmom -- kmom01

# 3. Check status
uv run task status

# 4. Implement your code in src/kmom01/
# ... write code ...

# 5. Run tests frequently
uv run task test -- kmom01

# 6. Check linting
uv run task lint

# 7. When ready, verify everything
uv run task check-ready -- kmom01

# 8. Commit and push
git add src/kmom01/
git commit -m "Complete kmom01 assignment"
git push origin kmom01

# 9. Create pull request on GitHub
# ... create PR ...

# 10. Optionally tag version
uv run task tag-version -- kmom01 1.0.0
git push origin v1.1.0.0
```

### Starting Assignment 2

```bash
# 1. Create branch from kmom01
uv run task start-kmom -- kmom02

# 2. Implement code in src/kmom02/
# ... write code ...

# 3. Test and verify
uv run task test -- kmom02
uv run task check-ready -- kmom02

# 4. Commit and push
git add src/kmom02/
git commit -m "Complete kmom02 assignment"
git push origin kmom02
```

### Fixing Previous Assignment

```bash
# 1. Switch to previous assignment
uv run task switch-kmom -- kmom01

# 2. Make fixes
# ... edit code ...

# 3. Test changes
uv run task test -- kmom01

# 4. Commit and push
git add src/kmom01/
git commit -m "Fix kmom01 issues"
git push origin kmom01

# 5. Return to current assignment
uv run task switch-kmom -- kmom02
```

---

## Tips & Best Practices

### Use Quick Tests During Development
```bash
# Run only structure tests first (faster)
uv run task test-struct -- kmom01

# Then run full tests
uv run task test -- kmom01
```

### Check Status Frequently
```bash
# See what you're working on
uv run task status
```

### Verify Before Submission
```bash
# One command to check everything
uv run task check-ready -- kmom01
```

### Use Help When Stuck
```bash
# Quick reference
uv run task help

# Full command list
uv run task --list
```

---

## Integration with GitHub Actions

The automated workflow (`.github/workflows/main.yml`) runs automatically on:
- Pull request events (labeled, opened, closed)
- Pull request reviews
- Version tags (`v[1-6].X.X`, `v10.X.X`)
- Issue comments

This validates your code using the same tests and linting rules you run locally.

---

## Troubleshooting

### "Branch already exists" error
Use `task switch-kmom` instead of `task start-kmom` to switch to existing branches.

### Tests not found
Run `uv run task download-tests` to ensure tests are up to date.

### Linting errors
Review errors with `uv run task lint`, then fix manually (auto-fix is disabled per course policy).

### "Not in correct directory" for labs
Lab download must be run from within the lab directory:
```bash
cd src/kmom01/lab_01
uv run task download-lab -- lab_01
```

---

## Summary of New Automation

### Commands Added
- **Testing**: `test`, `test-struct`, `test-extra`, `test-tag`, `test-quick`
- **Linting**: `lint`, `lint-all`, `format-check`, `format`
- **Branch Management**: `start-kmom`, `switch-kmom`, `branches`
- **Submission**: `check-ready`, `tag-version`
- **Workflow Helpers**: `status`, `setup`, `help`

### Key Benefits
1. **Simplified testing** - No need to remember pytest commands
2. **Automated branch workflow** - Correct source branch selection
3. **Readiness verification** - Single command to check submission status
4. **Consistent workflow** - Same commands for all assignments
5. **Clear next steps** - Status and help show what to do next

---

For the original student workflow instructions, see [README.md](README.md).
