"""Validate portable skill structure; does not contact Qiangua."""
from pathlib import Path
import re
import yaml


def validate(root):
    content = (root / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', content, re.S)
    if not match:
        raise ValueError('Missing YAML frontmatter')
    meta = yaml.safe_load(match.group(1))
    name = meta['name']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        raise ValueError('Invalid skill name')
    if root.name != name:
        raise ValueError('Directory must match skill name')
    desc = meta['description']
    if not isinstance(desc, str) or not 1 <= len(desc) <= 1024:
        raise ValueError('Invalid description')
    if not re.fullmatch(r'\d+\.\d+\.\d+', str(meta['metadata']['version'])):
        raise ValueError('Invalid version')
    for link in re.findall(r'\]\(([^)]+)\)', content):
        if '://' not in link and not (root / link.split('#')[0]).is_file():
            raise ValueError(f'Missing reference: {link}')
    ui = yaml.safe_load((root / 'agents/openai.yaml').read_text(encoding='utf-8'))
    if '$' + name not in ui['interface']['default_prompt']:
        raise ValueError('Invocation missing in default prompt')
    for required in ('README.md', 'CHANGELOG.md', 'references/result-schema.md'):
        if not (root / required).is_file():
            raise ValueError(f'Missing {required}')
    print(f'PASS: {name} {meta["metadata"]["version"]}')


if __name__ == '__main__':
    validate(Path(__file__).resolve().parents[1])
