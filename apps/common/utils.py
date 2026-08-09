import os
from pathlib import Path


def load_api_key(key_name="BAILIAN_API_KEY") -> str:
    api_key = os.getenv(key_name)
    if api_key:
        return api_key

    current_path = Path(__file__).resolve().parent
    env_path = None
    for directory in [current_path, *current_path.parents]:
        candidate = directory / ".env"
        if candidate.exists():
            env_path = candidate
            break

    if env_path is not None:
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            if key.strip() == key_name:
                return value.strip().strip("\"'")

    raise RuntimeError(f"请先设置环境变量 {key_name}，或在项目根目录或其父目录创建 .env 文件")
