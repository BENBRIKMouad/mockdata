import json
import os
import xml.sax.saxutils as saxutils
import xml.etree.ElementTree as ET

# Load baseline dataset
input_json = os.path.join(os.path.dirname(__file__), 'data', 'journal_mock.json')
with open(input_json, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Author emails map
author_emails = {
    "auth_01": "elena.vance@horizon-journal.internal",
    "auth_02": "julian.mercer@mercerdialogues.net",
    "auth_03": "maya.linchen@designsystems.org",
    "auth_04": "soren.lindqvist@scandicchronicles.se",
    "auth_05": "priya.ramanujan@cambridge-biotech.edu",
    "auth_06": "marcus.sterling@berlin-kernel.systems"
}

# Comment author emails and roles
commenter_meta = {
    "Marcus Sterling": {"email": "marcus.sterling@berlin-kernel.systems", "role": "VP of Infrastructure"},
    "Dr. Elena Vance": {"email": "elena.vance@horizon-journal.internal", "role": "Senior Research Fellow"},
    "Julian Mercer": {"email": "julian.mercer@mercerdialogues.net", "role": "Visiting Lecturer & Essayist"},
    "Maya Lin-Chen": {"email": "maya.linchen@designsystems.org", "role": "Head of Design Systems"},
    "Soren K. Lindqvist": {"email": "soren.lindqvist@scandicchronicles.se", "role": "Essayist & Photographer"},
    "Dr. Priya Ramanujan": {"email": "priya.ramanujan@cambridge-biotech.edu", "role": "Principal Investigator"},
    "Sarah Jenkins": {"email": "s.jenkins@rustacean.io", "role": "Senior Systems Engineer"},
    "Clara Oswald": {"email": "clara.oswald@hypermedia.ac.uk", "role": "Digital Anthropologist"},
    "Alex Thorne": {"email": "alex.thorne@spatialux.design", "role": "Lead Spatial Designer"},
    "Kenji Sato": {"email": "kenji.sato@kyotocraft.jp", "role": "Architect & Woodworker"},
    "Liam Gallagher": {"email": "liam.g@nordicwalks.org", "role": "Contributing Writer"},
    "David K. Vance": {"email": "d.vance@genomic-foundry.org", "role": "Bioinformatics Researcher"},
    "Dr. Aris Thorne": {"email": "aris.thorne@eth-zurich.ch", "role": "Microbiology Professor"},
    "Tobias Falke": {"email": "tobias.falke@munich-edge.de", "role": "Principal Site Reliability Engineer"},
    "Elena Vance": {"email": "elena.vance@horizon-journal.internal", "role": "Senior Research Fellow"},
    "Hannah Arendt Fan": {"email": "episteme.reader@oxford.edu", "role": "Postdoctoral Researcher in Epistemology"},
    "Devon Miller": {"email": "devon.miller@fluidtokens.io", "role": "Design Technologist"},
    "Kavita Rao": {"email": "kavita.rao@bangalore-tech.org", "role": "Staff Frontend Architect"},
    "Lucia Fernandez": {"email": "lucia.fernandez@stationery-chronicles.es", "role": "Archival Curator"},
    "Tomas Lind": {"email": "tomas.lind@gothenburg-press.se", "role": "Author & Editor"},
    "Prof. Arthur Pendelton": {"email": "a.pendelton@caltech.edu", "role": "Emeritus Chair in Chemical Physics"},
    "Zackary Moore": {"email": "zack.moore@p2p-labs.net", "role": "Decentralized Protocol Engineer"},
    "Rachel Adams": {"email": "rachel.adams@offline-first.dev", "role": "Local-First Core Contributor"}
}

def escape_xml(s):
    if s is None:
        return ""
    return saxutils.escape(str(s), {'"': "&quot;", "'": "&apos;"})

def cdata(s):
    if s is None:
        s = ""
    # Safe CDATA splitting if content contains ']]>'
    safe_s = str(s).replace("]]>", "]]]]><![CDATA[>")
    return f"<![CDATA[{safe_s}]]>"

authors = json_data.get('authors', [])
for a in authors:
    a['email'] = author_emails.get(a['id'], f"{a.get('username', 'author')}@horizon-journal.internal")

categories = json_data.get('categories', [])
entries = json_data.get('entries', [])

# Additional scheduled entries to fulfill requirement: status ('published', 'draft', 'scheduled')
scheduled_entry_1 = {
    "id": "post_013",
    "title": "Reactive Foundations in 2027: Signals, Fine-Grained Graphs, and Virtual DOM Twilight",
    "slug": "reactive-foundations-signals-fine-grained-graphs-2027",
    "summary": "An architectural retrospective and forward look into signal-based reactive graphs, compile-time reactivity, and why full tree reconciliation is quietly fading from the modern web landscape.",
    "cover_image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1600&q=85",
    "content": """# Reactive Foundations in 2027: Signals, Fine-Grained Graphs, and Virtual DOM Twilight

Over the past decade, web engineering has undergone three distinct evolutionary eras:
1. **The Direct Mutation Era** (jQuery, backbone view bindings)
2. **The Virtual DOM Era** (React, diffing trees, memoized reconciliation)
3. **The Fine-Grained Reactive Era** (Signals, Solid, Svelte 5 Runes, Vue Reactivity Core)

As application complexity surges and 120Hz display refresh budgets demand sub-8ms frame times, the overhead of whole-tree diffing has reached diminishing returns.

## The Problem with Whole-Tree Reconciliation

Virtual DOM was born to tame synchronous DOM churn. But its cost model assumes:
- Component functions re-execute from top to bottom.
- An intermediate virtual tree must be allocated and compared against previous state.
- Developers must manually manage dependency arrays (`useMemo`, `useCallback`) to prune re-renders.

```
State Change
   │
   ▼
[Component Hierarchy] ---> [Virtual DOM Diffing] ---> [DOM Mutations]
(Re-executes 40 sub-trees)  (Allocates tree nodes)   (Applies patch)
```

With **Signals**, dependencies are tracked at the atomic leaf level. When signal `count` emits, only the exact text node bound to `count` updates. The parent components never re-run.

## Signal Dependency Graphs

```typescript
// Architectural representation of atomic graph updates
class ReactiveSignal<T> {
  private subscribers = new Set<ReactiveComputation>();
  
  constructor(private value: T) {}

  get(): T {
    const active = Context.currentComputation;
    if (active) this.subscribers.add(active);
    return this.value;
  }

  set(next: T): void {
    if (next !== this.value) {
      this.value = next;
      this.notify();
    }
  }

  private notify(): void {
    for (const sub of this.subscribers) {
      sub.schedule();
    }
  }
}
```

## Looking Ahead

In 2027, reactivity is moving into the compiler layer. The browser no longer needs heavy framework runtimes; code compiles down to direct pinpoint mutations connected by topological reactive graphs.""",
    "author": authors[0], # Dr. Elena Vance
    "publication_date": "2026-11-05T09:00:00Z",
    "updated_at": "2026-10-25T11:20:00Z",
    "read_time": 7,
    "status": "scheduled",
    "featured": True,
    "categories": ["Technology"],
    "tags": ["reactivity", "signals", "web-performance", "compilers", "javascript"],
    "metrics": {
        "views": 0,
        "likes": 0,
        "claps": 0,
        "shares": 0,
        "bookmarks": 45,
        "comments_count": 1
    },
    "comments": [
        {
            "id": "comm_01301",
            "author": {
                "name": "Marcus Sterling",
                "username": "msterling",
                "avatar": authors[5]["avatar"]
            },
            "content": "Looking forward to this scheduled drop! The comparison with compiler-directed graph scheduling hits the exact pain points we hit with high-frequency telemetry dashboards.",
            "created_at": "2026-10-26T16:00:00Z",
            "likes": 8,
            "replies": []
        }
    ]
}

scheduled_entry_2 = {
    "id": "post_014",
    "title": "Acoustic Ecology of Modern Workspaces: Silence, Texture, and Calm Hardware",
    "slug": "acoustic-ecology-modern-workspaces-calm-hardware",
    "summary": "Exploring the psychoacoustics of workspace design: from fanless passive computing and mechanical dampening to soundscapes that foster deep attention rather than auditory fatigue.",
    "cover_image": "https://images.unsplash.com/photo-1516455590571-18256e5bb9ff?auto=format&fit=crop&w=1600&q=85",
    "content": """# Acoustic Ecology of Modern Workspaces: Silence, Texture, and Calm Hardware

The modern studio is permeated by an invisible, relentless hum: high-RPM server fans, coil whine from high-wattage charging bricks, hard drive seek chatter, and air conditioning drones.

While ergonomics has obsessively optimized lumbar support and monitor elevation, **acoustic ergonomics** remains the neglected sensory dimension of cognitive work.

## 1. The Psychoacoustic Toll of Background Noise

Decibels measure sound pressure, but psychoacoustics measures cognitive toll:
- Constant 45dB white noise raises cortisol and reduces working memory bandwidth by up to 18%.
- High-frequency coil whine triggers subconscious micro-arousal states, disrupting flow states.
- Auditory distraction takes on average 23 minutes to recover from fully.

## 2. The Return of Calm Hardware

In recent years, an architectural rebellion has quietly gained momentum:
- **Zero-RPM Fanless Systems**: Passive dissipation chassis machined from solid aluminum billets that function as monolithic heat sinks.
- **Acoustic Gasket-Mounted Peripherals**: Keyboards engineered with silicone dampeners and lubricated switches designed for soft thuds rather than high-pitched clatter.
- **Tactile Sound Absorption**: Felt acoustic baffles, cork surfaces, and unpolished cedar walls that naturally diffuse reverberations.

> "A truly professional workspace does not announce its power through roar and light; it disappears into reverent silence."

## 3. Designing for Auditory Restoration

To build an acoustically restorative environment, one must treat silence not as an absence, but as a textured material. Incorporate soft textiles, manage reflective glass planes, and insist on silent silicon.""",
    "author": authors[1], # Julian Mercer
    "publication_date": "2026-11-12T14:30:00Z",
    "updated_at": "2026-10-26T19:40:00Z",
    "read_time": 6,
    "status": "scheduled",
    "featured": False,
    "categories": ["Philosophy", "Design"],
    "tags": ["acoustic-ecology", "calm-tech", "ergonomics", "hardware", "analog-living", "workplace-design"],
    "metrics": {
        "views": 0,
        "likes": 0,
        "claps": 0,
        "shares": 0,
        "bookmarks": 31,
        "comments_count": 0
    },
    "comments": []
}

entries.append(scheduled_entry_1)
entries.append(scheduled_entry_2)

# Calculate statistics
total_entries = len(entries)
published_count = len([e for e in entries if e.get("status") == "published"])
draft_count = len([e for e in entries if e.get("status") == "draft"])
scheduled_count = len([e for e in entries if e.get("status") == "scheduled"])
featured_count = len([e for e in entries if e.get("featured") is True])
total_authors = len(authors)
total_categories = len(categories)

def count_all_comments(comment_list):
    cnt = len(comment_list)
    for c in comment_list:
        cnt += count_all_comments(c.get("replies", []))
    return cnt

total_comments = sum(count_all_comments(e.get("comments", [])) for e in entries)
total_views = sum(e.get("metrics", {}).get("views", 0) for e in entries)
total_likes = sum(e.get("metrics", {}).get("likes", 0) for e in entries)
total_bookmarks = sum(e.get("metrics", {}).get("bookmarks", 0) for e in entries)

lines = []
lines.append('<?xml version="1.0" encoding="UTF-8"?>')
lines.append('<journal version="1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">')

# Metadata block
lines.append('  <metadata>')
lines.append('    <title>The Horizon Journal &amp; Publication Hub</title>')
lines.append('    <subtitle>Perspectives on Systems Architecture, Digital Philosophy, Design Systems, and Science</subtitle>')
lines.append('    <description>Comprehensive mock dataset for modern journal and publishing platforms featuring rich markdown content, authors, categories, metrics, and threaded discussions.</description>')
lines.append('    <siteUrl>https://horizon-journal.internal</siteUrl>')
lines.append('    <feedUrl>https://horizon-journal.internal/feed.xml</feedUrl>')
lines.append('    <language>en-US</language>')
lines.append('    <copyright>© 2026 The Horizon Journal contributors. All rights reserved.</copyright>')
lines.append('    <generator>Horizon Publisher XML Engine v2.4</generator>')
lines.append('    <generatedAt>2026-10-26T23:30:00Z</generatedAt>')
lines.append('    <statistics>')
lines.append(f'      <totalEntries>{total_entries}</totalEntries>')
lines.append(f'      <publishedCount>{published_count}</publishedCount>')
lines.append(f'      <draftCount>{draft_count}</draftCount>')
lines.append(f'      <scheduledCount>{scheduled_count}</scheduledCount>')
lines.append(f'      <featuredCount>{featured_count}</featuredCount>')
lines.append(f'      <totalAuthors>{total_authors}</totalAuthors>')
lines.append(f'      <totalCategories>{total_categories}</totalCategories>')
lines.append(f'      <totalComments>{total_comments}</totalComments>')
lines.append(f'      <totalViews>{total_views}</totalViews>')
lines.append(f'      <totalLikes>{total_likes}</totalLikes>')
lines.append(f'      <totalBookmarks>{total_bookmarks}</totalBookmarks>')
lines.append('    </statistics>')
lines.append('  </metadata>')

# Authors block
lines.append('  <authors>')
for a in authors:
    lines.append(f'    <author id="{escape_xml(a.get("id"))}">')
    lines.append(f'      <name>{escape_xml(a.get("name"))}</name>')
    lines.append(f'      <email>{escape_xml(a.get("email"))}</email>')
    lines.append(f'      <username>{escape_xml(a.get("username"))}</username>')
    lines.append(f'      <role>{escape_xml(a.get("role"))}</role>')
    lines.append(f'      <avatar>{escape_xml(a.get("avatar"))}</avatar>')
    lines.append(f'      <bio>{escape_xml(a.get("bio"))}</bio>')
    lines.append(f'      <location>{escape_xml(a.get("location"))}</location>')
    social = a.get("social", {})
    if social:
        lines.append('      <social>')
        for platform, url in social.items():
            lines.append(f'        <link platform="{escape_xml(platform)}">{escape_xml(url)}</link>')
        lines.append('      </social>')
    lines.append('    </author>')
lines.append('  </authors>')

# Categories block
lines.append('  <categories>')
for c in categories:
    lines.append(f'    <category id="{escape_xml(c.get("id"))}" slug="{escape_xml(c.get("slug"))}">')
    lines.append(f'      <name>{escape_xml(c.get("name"))}</name>')
    lines.append(f'      <slug>{escape_xml(c.get("slug"))}</slug>')
    lines.append(f'      <color>{escape_xml(c.get("color"))}</color>')
    lines.append(f'      <description>{escape_xml(c.get("description"))}</description>')
    lines.append('    </category>')
lines.append('  </categories>')

# Comment serializer helper
def serialize_comment(c, indent_level=8, in_reply_to=None):
    c_lines = []
    ind = " " * indent_level
    c_id = escape_xml(c.get("id", ""))
    in_reply_attr = f' inReplyTo="{escape_xml(in_reply_to)}"' if in_reply_to else ""
    c_lines.append(f'{ind}<comment id="{c_id}"{in_reply_attr}>')
    
    author_info = c.get("author", {})
    c_name = author_info.get("name", "Anonymous")
    meta = commenter_meta.get(c_name, {})
    c_email = meta.get("email", f"{c_name.lower().replace(' ', '.')}@horizon-community.org")
    c_role = meta.get("role", "Reader & Contributor")
    c_avatar = author_info.get("avatar", "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=400&q=80")

    c_lines.append(f'{ind}  <author>')
    c_lines.append(f'{ind}    <name>{escape_xml(c_name)}</name>')
    c_lines.append(f'{ind}    <email>{escape_xml(c_email)}</email>')
    c_lines.append(f'{ind}    <role>{escape_xml(c_role)}</role>')
    c_lines.append(f'{ind}    <avatar>{escape_xml(c_avatar)}</avatar>')
    c_lines.append(f'{ind}  </author>')
    c_lines.append(f'{ind}  <createdAt>{escape_xml(c.get("created_at"))}</createdAt>')
    c_lines.append(f'{ind}  <likes>{c.get("likes", 0)}</likes>')
    c_lines.append(f'{ind}  <content>{cdata(c.get("content", ""))}</content>')

    replies = c.get("replies", [])
    if replies:
        c_lines.append(f'{ind}  <replies count="{len(replies)}">')
        for r in replies:
            c_lines.extend(serialize_comment(r, indent_level + 4, in_reply_to=c_id))
        c_lines.append(f'{ind}  </replies>')
    else:
        c_lines.append(f'{ind}  <replies count="0" />')

    c_lines.append(f'{ind}</comment>')
    return c_lines

# Entries block
lines.append('  <entries>')
for entry in entries:
    e_id = escape_xml(entry.get("id"))
    status = escape_xml(entry.get("status", "draft"))
    is_featured = "true" if entry.get("featured") else "false"
    
    lines.append(f'    <entry id="{e_id}" status="{status}" featured="{is_featured}">')
    lines.append(f'      <id>{e_id}</id>')
    lines.append(f'      <title>{escape_xml(entry.get("title"))}</title>')
    lines.append(f'      <slug>{escape_xml(entry.get("slug"))}</slug>')
    lines.append(f'      <summary>{cdata(entry.get("summary", ""))}</summary>')
    lines.append(f'      <content format="markdown" encoding="cdata">{cdata(entry.get("content", ""))}</content>')
    
    if entry.get("cover_image"):
        lines.append(f'      <coverImage alt="{escape_xml(entry.get("title"))} Cover">{escape_xml(entry.get("cover_image"))}</coverImage>')

    # Author details
    e_author = entry.get("author", {})
    a_id = escape_xml(e_author.get("id", ""))
    a_id_attr = f' id="{a_id}"' if a_id else ""
    lines.append(f'      <author{a_id_attr}>')
    lines.append(f'        <name>{escape_xml(e_author.get("name"))}</name>')
    lines.append(f'        <email>{escape_xml(e_author.get("email", author_emails.get(a_id, "editorial@horizon-journal.internal")))}</email>')
    lines.append(f'        <role>{escape_xml(e_author.get("role", "Contributor"))}</role>')
    lines.append(f'        <avatar>{escape_xml(e_author.get("avatar"))}</avatar>')
    lines.append('      </author>')

    # Dates
    lines.append(f'      <publicationDate>{escape_xml(entry.get("publication_date"))}</publicationDate>')
    lines.append(f'      <updatedDate>{escape_xml(entry.get("updated_at"))}</updatedDate>')

    # Read time
    rt = entry.get("read_time", 5)
    lines.append(f'      <readTime minutes="{rt}">{rt}</readTime>')

    # Status & Featured
    lines.append(f'      <status>{status}</status>')
    lines.append(f'      <featured>{is_featured}</featured>')

    # Categories
    lines.append('      <categories>')
    for cat_name in entry.get("categories", []):
        cat_slug = cat_name.lower().replace(" ", "-")
        lines.append(f'        <category slug="{escape_xml(cat_slug)}">{escape_xml(cat_name)}</category>')
    lines.append('      </categories>')

    # Tags
    lines.append('      <tags>')
    for tag in entry.get("tags", []):
        lines.append(f'        <tag>{escape_xml(tag)}</tag>')
    lines.append('      </tags>')

    # Metrics
    m = entry.get("metrics", {})
    lines.append('      <metrics>')
    lines.append(f'        <views>{m.get("views", 0)}</views>')
    lines.append(f'        <likes>{m.get("likes", 0)}</likes>')
    lines.append(f'        <claps>{m.get("claps", m.get("likes", 0))}</claps>')
    lines.append(f'        <bookmarks>{m.get("bookmarks", 0)}</bookmarks>')
    lines.append(f'        <shares>{m.get("shares", 0)}</shares>')
    lines.append(f'        <commentsCount>{m.get("comments_count", 0)}</commentsCount>')
    lines.append('      </metrics>')

    # Threaded Comments
    comments = entry.get("comments", [])
    total_entry_comments = count_all_comments(comments)
    if comments:
        lines.append(f'      <comments count="{total_entry_comments}">')
        for comment in comments:
            lines.extend(serialize_comment(comment, indent_level=8))
        lines.append('      </comments>')
    else:
        lines.append(f'      <comments count="0" />')

    lines.append('    </entry>')

lines.append('  </entries>')
lines.append('</journal>')
lines.append('') # trailing newline

xml_content = "\n".join(lines)

output_xml_path = os.path.join(os.path.dirname(__file__), 'data', 'journal_mock.xml')
with open(output_xml_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(xml_content)

print(f"Generated XML file at: {output_xml_path}")
print(f"File size: {os.path.getsize(output_xml_path)} bytes")

# Validation check
try:
    tree = ET.parse(output_xml_path)
    root = tree.getroot()
    print("XML Validation: SUCCESS (Well-formed and parsed successfully by xml.etree.ElementTree)")
    print(f"Root tag: {root.tag}, version attribute: {root.attrib.get('version')}")
    entries_found = root.findall('.//entry')
    print(f"Found {len(entries_found)} entries in parsed XML.")
except Exception as e:
    print(f"XML Validation FAILED: {e}")
    raise
