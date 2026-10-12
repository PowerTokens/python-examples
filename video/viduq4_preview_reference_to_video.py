"""Vidu Q4 preview reference-to-video via PowerTokens native Vidu endpoints.

Model id: viduq4-preview
Docs: https://docs.powertokens.ai/en/zmodelVideo/vidu/viduq4-preview-reference-to-video
Run: POWERTOKENS_API_KEY=... python video/viduq4_preview_reference_to_video.py
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

API = "https://api.powertokens.ai"
KEY = os.environ.get("POWERTOKENS_API_KEY")
if not KEY:
    raise SystemExit("Set POWERTOKENS_API_KEY")


def request(method: str, path: str, body: dict | None = None) -> dict:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        f"{API}{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {KEY}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{method} {path} -> {e.code}: {e.read().decode()}") from e


created = request(
    "POST",
    "/vidu/ent/v2/reference2video",
    {
        "model": "viduq4-preview",
        "images": [
            "https://prod-ss-images.s3.cn-northwest-1.amazonaws.com.cn/vidu-maas/template/reference2video-1.png",
        ],
        "prompt": (
            "Cinematic shot: an astronaut walks slowly on the lunar surface, "
            "camera pulls back from close-up to wide shot."
        ),
        "duration": 5,
        "aspect_ratio": "16:9",
        "resolution": "720p",
    },
)
print("submitted", created)
task_id = created["task_id"]

for _ in range(60):
    time.sleep(5)
    status = request("GET", f"/vidu/ent/v2/tasks/{task_id}/creations")
    print("state", status.get("state"))
    if status.get("state") == "success":
        creations = status.get("creations") or []
        print("video", (creations[0] or {}).get("url") if creations else None)
        break
    if status.get("state") == "failed":
        raise SystemExit(f"task failed: {status.get('err_code') or 'unknown'}")
