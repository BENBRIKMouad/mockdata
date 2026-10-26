<div align="center">
  <img src="assets/icon.svg" width="72" height="72" alt="Horizon Journal Logo" />
  <h1>Horizon Journal Mock Dataset</h1>
  <p><strong>A production-grade, multi-format mock dataset for modern technical journals, publishing platforms, and CMS benchmarking.</strong></p>

  <p>
    <a href="#available-formats"><img src="https://img.shields.io/badge/Formats-XML%20%7C%20JSON%20%7C%20CSV%20%7C%20Markdown-0891b2?style=flat-square" alt="Formats" /></a>
    <a href="#schema--structure"><img src="https://img.shields.io/badge/Status-Published%20%7C%20Draft%20%7C%20Scheduled-10b981?style=flat-square" alt="Statuses" /></a>
    <a href="#scripts"><img src="https://img.shields.io/badge/Python-3.10%2B-3b82f6?style=flat-square" alt="Python" /></a>
    <a href="#license"><img src="https://img.shields.io/badge/License-MIT-gray?style=flat-square" alt="License" /></a>
  </p>
</div>

---

## 📖 Overview

The **Horizon Journal Mock Dataset** is a comprehensive, realistic content collection designed to accelerate the development, prototyping, and testing of modern blogging engines, headless CMSs, reading platforms, and search pipelines.

Unlike bare-bones filler text, entries feature thoughtful long-form technical and philosophical writing across systems architecture, human-computer interaction, distributed software, biophysics, and design systems—complete with code snippets, architecture diagrams, rich metadata, metrics, and multi-tier threaded discussions.

---

## 📁 Available Formats

All datasets are located in the [`data/`](file:///C:/Users/mouad_benbrik/.t3/projects/subagent/data) directory:

| File | Format | Size | Description | Best For |
| :--- | :---: | :---: | :--- | :--- |
| [`data/journal_mock.xml`](file:///C:/Users/mouad_benbrik/.t3/projects/subagent/data/journal_mock.xml) | **XML 1.0** | ~80 KB | Structured XML with `CDATA` rich text, author entities, metadata stats, and nested comments. | RSS/Atom feeds, XML importers, legacy feed syndication. |
| [`data/journal_mock.json`](file:///C:/Users/mouad_benbrik/.t3/projects/subagent/data/journal_mock.json) | **JSON** | ~65 KB | Fully typed document with schema validation, nested author records, metrics, and threaded arrays. | REST/GraphQL APIs, Next.js/Nuxt state, MongoDB/PostgreSQL JSONB. |
| [`data/journal_mock.csv`](file:///C:/Users/mouad_benbrik/.t3/projects/subagent/data/journal_mock.csv) | **CSV** | ~25 KB | 26 normalized article rows with comma-separated tags, view counts, and authors. | SQL databases, spreadsheets, Python pandas, search indexing. |
| [`data/journal_mock.md`](file:///C:/Users/mouad_benbrik/.t3/projects/subagent/data/journal_mock.md) | **Markdown** | ~21 KB | Multi-document collection formatted with YAML frontmatter and GitHub-flavored markdown. | Static site generators (Astro, Next.js Contentlayer, Hugo, 11ty). |

---

## 🧩 Schema & Features

### 1. Document Entity Structure
Each entry contains comprehensive editorial metadata:
* **Identities**: Unique ID (`post_001`), descriptive title, SEO-friendly URL slug.
* **Content**: Lead summary / excerpt, full markdown article body (`CDATA` protected in XML) with code blocks, blockquotes, and tables.
* **Author Details**: Full name, username, email address, role/title, avatar photo, and social links.
* **Publishing Lifecycle**: Statuses include `published`, `draft`, and `scheduled` with publication and last updated timestamps.
* **Taxonomy**: Hierarchical categories (*Technology*, *Philosophy*, *Design*, *Daily Reflections*, *Science*) and normalized keyword tags.
* **Engagement Metrics**: Realistic view counts, likes, claps, bookmarks, shares, and comment counters.
* **Threaded Discussions**: Nested comment threads featuring authors, timestamps, like counts, and parent-child reply relationships (`inReplyTo`).

### 2. Status Distribution
* **Published** (10 entries): Live articles with complete engagement metrics and discussion threads.
* **Draft** (2 entries): In-progress articles without engagement data, ideal for preview mode testing.
* **Scheduled** (2 entries): Future publication dates designed to test scheduled job runners and release queues.

---

## 🚀 Quick Start & Usage

### Python (Loading XML)
```python
import xml.etree.ElementTree as ET

# Parse the XML dataset
tree = ET.parse("data/journal_mock.xml")
root = tree.getroot()

# Query metadata statistics
total = root.findtext("metadata/statistics/totalEntries")
print(f"Total entries: {total}")

# Iterate over published articles
for entry in root.findall(".//entry[@status='published']"):
    title = entry.findtext("title")
    author = entry.findtext("author/name")
    read_time = entry.find("readTime").attrib.get("minutes")
    print(f"- {title} by {author} ({read_time} min)")
```

### Python (Loading JSON)
```python
import json

with open("data/journal_mock.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)

for post in dataset["entries"]:
    print(f"[{post['status'].upper()}] {post['title']}")
```

### TypeScript / JavaScript (Node & Browser)
```typescript
import fs from "fs";

interface JournalEntry {
  id: string;
  title: string;
  slug: string;
  status: "published" | "draft" | "scheduled";
  read_time: number;
  author: { name: string; email: string; avatar: string };
  metrics: { views: number; likes: number; comments_count: number };
}

const raw = fs.readFileSync("data/journal_mock.json", "utf-8");
const { entries }: { entries: JournalEntry[] } = JSON.parse(raw);

const featured = entries.filter((e) => e.status === "published" && e.read_time > 7);
console.log(`Found ${featured.length} in-depth featured articles`);
```

---

## 🛠️ Generating & Modifying Data

The dataset generation scripts are included in the repository root:

* **Generate Both JSON and XML**:
  ```bash
  python generate.py
  ```
* **Generate XML Only**:
  ```bash
  python generate_xml.py
  ```

The generator will validate the resulting XML tree structure with `xml.etree.ElementTree` and ensure correct UTF-8 encoding.

---

## 📂 Project Structure

```
mockdata/
├── assets/
│   └── icon.svg              # Repository icon
├── data/
│   ├── journal_mock.csv      # Tabular CSV export (26 articles)
│   ├── journal_mock.json     # JSON schema dataset (12 articles)
│   ├── journal_mock.md       # Markdown + YAML frontmatter articles
│   └── journal_mock.xml      # Full XML 1.0 dataset (14 articles)
├── generate.py               # Main generator pipeline
├── generate_xml.py           # XML serializer & ElementTree validator
└── README.md                 # Project documentation
```

---

## 📄 License

This dataset and generator scripts are licensed under the [MIT License](LICENSE).
Feel free to use this data in open source projects, automated test suites, product demos, and benchmarks.
