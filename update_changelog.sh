#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

printf "# AI CHANGELOG\n\n" > temp.md

OUTPUT=$(python ai_changelog/update.py)
printf "%s\n\n" "$OUTPUT" >> temp.md

if [[ -f AI_CHANGELOG.md ]]; then
  git checkout AI_CHANGELOG.md  # To rollback the previous additions
  tail -n +3 AI_CHANGELOG.md >> temp.md
fi

mv temp.md AI_CHANGELOG.md
git add AI_CHANGELOG.md
