# Leetcode_Solutions

This repository contains my personal collection of LeetCode problem solutions, automatically synced from my LeetCode account using glsync workflow.

The goal of this repository is to:
- Track problem-solving progress over time
- Maintain a clean and organized archive of solutions
- Reflect consistent coding activity on GitHub using actual submission timestamps

---

## How It Works

This repository is powered by a CLI tool called `glsync`, which:
- Fetches all my accepted LeetCode submissions
- Preserves original submission timestamps
- Commits each solution into this repository
- Pushes everything to GitHub in chronological order

This creates a realistic contribution history that reflects actual practice.

---

## Repository Structure

Solutions are organized automatically based on LeetCode problem metadata. Each problem typically includes:
- Problem name
- Solution code
- Language used

---

## Problem Table

<!-- START_TABLE -->
| # | Problem Name | Language | File |
|---|--------------|----------|------|
| 1 | Two Sum | Python | [FILE](1%20Two%20Sum) |
| 9 | Palindrome Number | Java | [FILE](9%20Palindrome%20Number) |
| 175 | Combine Two Tables | SQL | [FILE](175%20Combine%20Two%20Tables) |
| 282 | Expression Add Operators | Python | [FILE](282%20Expression%20Add%20Operators) |
| 338 | Counting Bits | Python | [FILE](338%20Counting%20Bits) |
| 1438 | Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit | Python | [FILE](1438%20Longest%20Continuous%20Subarray%20With%20Absolute%20Diff%20Less%20Than%20or%20Equal%20to%20Limit) |

<!-- END_TABLE -->

> As new solutions are added via `glsync`, this table will grow accordingly.

---

## Sync Script (`sync_leetcode.sh`)

To simplify syncing, this repository includes a helper script:

### Usage

```bash
./sync_leetcode.sh
