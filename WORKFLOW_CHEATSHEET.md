# Workflow Automation - Quick Reference

## 🚀 First Time Setup
```bash
uv run task setup
uv run task start-kmom -- kmom01
```

## 📝 Daily Development
```bash
# Check where you are
uv run task status

# Switch assignments
uv run task switch-kmom -- kmom01

# Test your code
uv run task test -- kmom01
uv run task test-struct -- kmom01   # Structure only (faster)

# Check code quality
uv run task lint
```

## ✅ Before Submitting
```bash
# Verify everything is ready
uv run task check-ready -- kmom01

# Commit and push
git add src/kmom01/
git commit -m "Complete kmom01"
git push origin kmom01

# Optional: Tag version
uv run task tag-version -- kmom01 1.0.0
git push origin v1.1.0.0
```

## 🔄 Starting Next Assignment
```bash
uv run task start-kmom -- kmom02
```

## 🆘 Need Help?
```bash
uv run task help          # Categorized help
uv run task --list        # All commands
uv run task status        # Your current state
```

## 📥 Update Files
```bash
uv run task download-tests          # Update tests
uv run task download-ruff-config    # Update linting rules
```

---

**Full Documentation**: See [WORKFLOW_AUTOMATION.md](WORKFLOW_AUTOMATION.md)
