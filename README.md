# Leetcode_Solutions

This repository contains my personal collection of LeetCode problem solutions, automatically synced from my LeetCode account using glsync workflow.

The goal of this repository is to:
- Track problem-solving progress over time
- Maintain a clean and organized archive of solutions
- Reflect consistent coding activity on GitHub using actual submission timestamps

---

## 🚀 How It Works

This repository is powered by a CLI tool called `glsync`, which:
- Fetches all my accepted LeetCode submissions
- Preserves original submission timestamps
- Commits each solution into this repository
- Pushes everything to GitHub in chronological order

This creates a realistic contribution history that reflects actual practice.

---

## 📂 Repository Structure

Solutions are organized automatically based on LeetCode problem metadata. Each problem typically includes:
- Problem name
- Solution code
- Language used

---

## 📜 Table of Contents

> ⚠️ This section is designed to scale automatically as new problems are synced.

| Problem Name | Language | Description |
|-------------|----------|------------|
| Two Sum | Python | Uses a hashmap to find two numbers that add up to a target in linear time |
| Add Two Numbers | Python | Linked list addition with carry handling |
| Longest Substring Without Repeating Characters | Python | Sliding window with set/hashmap |
| ... | ... | ... |

> As new solutions are added via `glsync`, this table will grow accordingly.

---

## 🔄 Sync Script (`sync_leetcode.sh`)

To simplify syncing, this repository includes a helper script:

### Usage

```bash
./sync_leetcode.sh
