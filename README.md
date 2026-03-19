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
| Problem Name | Language | File |
|-------------|----------|------|
| 1438Longest-Continuous-Subarray-With-Absolute-Diff-Less-Than-Or-Equal-To-Limit | py | [./1438 Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit/1438longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.py](./1438 Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit/1438longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.py) |
| 1Two-Sum | py | [./1 Two Sum/1two-sum.py](./1 Two Sum/1two-sum.py) |
| 282Expression-Add-Operators | py | [./282 Expression Add Operators/282expression-add-operators.py](./282 Expression Add Operators/282expression-add-operators.py) |
| 338Counting-Bits | py | [./338 Counting Bits/338counting-bits.py](./338 Counting Bits/338counting-bits.py) |
| 9Palindrome-Number | java | [./9 Palindrome Number/9palindrome-number.java](./9 Palindrome Number/9palindrome-number.java) |
| Generate Readme | py | [./generate_readme.py](./generate_readme.py) |

<!-- END_TABLE -->

> As new solutions are added via `glsync`, this table will grow accordingly.

---

## Sync Script (`sync_leetcode.sh`)

To simplify syncing, this repository includes a helper script:

### Usage

```bash
./sync_leetcode.sh
