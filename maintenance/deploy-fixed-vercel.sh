#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
staging_root="$(mktemp -d /private/tmp/chatgpt-codex-enterprise-settings-g.XXXXXX)"
staging_dir="$staging_root/project"

cleanup() {
  rm -rf "$staging_root"
}
trap cleanup EXIT

project_name="chatgpt-codex-enterprise-settings-guide"
project_id="prj_EcjXqmGIjGTzSxyMQjq8LhB019l3"
org_id="team_zxpJ0h11ZO3bDEByeNvLDELu"
scope="jaewonjung-bits-projects"

mkdir -p "$staging_dir/.vercel"

# Copy the repo into a lowercase temp directory so Vercel never derives an
# invalid project name from a worktree path with spaces or uppercase letters.
tar -C "$repo_root" \
  --exclude='.git' \
  --exclude='.vercel' \
  -cf - . | tar -C "$staging_dir" -xf -

cat > "$staging_dir/.vercel/project.json" <<EOF
{"projectId":"$project_id","orgId":"$org_id","projectName":"$project_name"}
EOF

echo "Deploying to fixed Vercel project: $project_name"
echo "Alias target: https://chatgpt-codex-enterprise-settings-g.vercel.app/"

vercel deploy "$staging_dir" --prod -y --scope "$scope"
