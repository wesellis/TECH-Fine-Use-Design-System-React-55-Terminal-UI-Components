# 🎨 Fine Use Design System
### React Terminal UI Components for Modern Developer Tools

[![React](https://img.shields.io/badge/React-18.0+-61DAFB?style=for-the-badge&logo=react)](https://reactjs.org)
[![Components](https://img.shields.io/badge/Components-55+-brightgreen?style=for-the-badge)](https://github.com)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=for-the-badge&logo=typescript)](https://www.typescriptlang.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## 🎯 Overview

Comprehensive React component library with **55+ terminal-style UI components** for building developer tools, CLI interfaces, and retro-themed applications. Save weeks of development time with pre-built, customizable components that just work.

### 📊 What's Included

| Category | Components | Purpose |
|----------|------------|---------|
| **Input** | 12 components | Terminal inputs, command prompts |
| **Display** | 15 components | Code blocks, logs, outputs |
| **Navigation** | 8 components | File trees, tabs, menus |
| **Feedback** | 10 components | Progress bars, spinners, alerts |
| **Layout** | 10 components | Panels, splits, grids |

## 💡 Perfect For

- **Developer Tools**: IDEs, code editors, debuggers
- **Admin Dashboards**: Server monitoring, log viewers
- **CLI Applications**: Web-based terminals, REPLs
- **Retro Themes**: Hacker aesthetics, vintage computing
- **Educational Tools**: Coding tutorials, interactive lessons

## ⚡ Quick Start

```bash
# Install
npm install fine-use-design-system

# Import components
import { Terminal, CodeBlock, FileTree } from 'fine-use-design-system';

# Use in your app
<Terminal
  prompt="$"
  commands={['ls', 'cd', 'git']}
  onCommand={handleCommand}
/>
```

## 🎨 Component Examples

### Terminal Component
```jsx
<Terminal
  theme="matrix"
  fontSize={14}
  promptSymbol=">"
  history={commandHistory}
  autocomplete={true}
/>
```

### Code Editor
```jsx
<CodeEditor
  language="javascript"
  theme="monokai"
  lineNumbers={true}
  highlightActiveLine={true}
  value={code}
  onChange={setCode}
/>
```

### File Tree
```jsx
<FileTree
  data={projectStructure}
  onSelect={handleFileSelect}
  expandedPaths={['/src', '/components']}
  showIcons={true}
/>
```

## 🎨 Themes

10 built-in themes:
- **Classic**: Green on black
- **Matrix**: Matrix rain effect
- **Dracula**: Purple and pink
- **Monokai**: Classic editor theme
- **Synthwave**: 80s neon
- **Cyberpunk**: Futuristic glow
- **Amber**: Vintage CRT
- **Nord**: Arctic blue
- **Solarized**: Easy on eyes
- **Custom**: Build your own

## 📦 All Components

### Input Components
- Terminal
- CommandInput
- SearchBar
- CodeInput
- PasswordField
- AutoComplete
- CommandPalette
- KeyboardInput
- FileUploader
- FormBuilder
- QueryBuilder
- ShortcutMapper

### Display Components
- CodeBlock
- LogViewer
- JSONViewer
- DiffViewer
- MarkdownRenderer
- SyntaxHighlighter
- DataTable
- TreeView
- GraphVisualizer
- HexViewer
- BinaryDisplay
- ASCIIArt
- MatrixRain
- ProgressLog
- OutputPanel

### Navigation
- FileExplorer
- Breadcrumbs
- TabBar
- Sidebar
- ContextMenu
- CommandMenu
- StatusBar
- ToolBar

### Feedback
- ProgressBar
- Spinner
- Toast
- Alert
- LoadingDots
- PulseIndicator
- StatusLight
- ErrorBoundary
- SuccessCheck
- TypeWriter

### Layout
- SplitPane
- Panel
- Window
- Grid
- Dock
- Workspace
- Canvas
- Overlay
- Modal
- Drawer

## 🛠️ Customization

```jsx
// Custom theme
const customTheme = {
  background: '#0a0e27',
  foreground: '#00ff41',
  accent: '#ff006e',
  fontFamily: 'Fira Code',
  fontSize: 14
};

<ThemeProvider theme={customTheme}>
  <App />
</ThemeProvider>
```

## 📈 Performance

- **Bundle Size**: 45KB gzipped (tree-shakeable)
- **Render Speed**: 60fps animations
- **Accessibility**: WCAG 2.1 AA compliant
- **Browser Support**: Chrome, Firefox, Safari, Edge
- **Mobile Ready**: Touch-optimized

## 🔧 Advanced Features

### Keyboard Shortcuts
```jsx
<ShortcutProvider shortcuts={customShortcuts}>
  <Terminal />
</ShortcutProvider>
```

### State Management
```jsx
// Built-in state management
const { history, addCommand, clearHistory } = useTerminalState();
```

### Plugins
```jsx
// Extend functionality
<Terminal plugins={[GitPlugin, DockerPlugin, CustomPlugin]} />
```

## 📚 Documentation

Full documentation at [fine-use.dev](https://fine-use.dev)

- [Getting Started](https://fine-use.dev/docs/getting-started)
- [Component API](https://fine-use.dev/docs/api)
- [Theming Guide](https://fine-use.dev/docs/theming)
- [Examples](https://fine-use.dev/examples)
- [Playground](https://fine-use.dev/playground)

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

```bash
# Development setup
git clone https://github.com/yourusername/fine-use-design-system
npm install
npm run storybook
```

## 📜 License

MIT License - Free for personal and commercial use

---

<div align="center">

**Build Terminal UIs Faster**

[![npm](https://img.shields.io/npm/v/fine-use-design-system?style=for-the-badge)](https://www.npmjs.com/package/fine-use-design-system)
[![Downloads](https://img.shields.io/npm/dm/fine-use-design-system?style=for-the-badge)](https://www.npmjs.com/package/fine-use-design-system)

</div>