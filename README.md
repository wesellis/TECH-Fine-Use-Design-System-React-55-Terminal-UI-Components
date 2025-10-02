# Fine Use Design System

React component library for building terminal-style user interfaces.

[![React](https://img.shields.io/badge/React-18.0+-61DAFB?style=flat-square&logo=react)](https://reactjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=flat-square&logo=typescript)](https://www.typescriptlang.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

## Overview

A collection of React components for creating terminal-style interfaces. Useful for developer tools, CLI applications, and retro-themed web apps.

## Features

- **Terminal UI Components** - Input fields, command prompts, code blocks
- **Multiple Themes** - Classic green, Matrix, Dracula, Synthwave, and more
- **TypeScript Support** - Full type definitions included
- **Customizable** - Theme system with CSS variables
- **Responsive** - Works on desktop and mobile

## Installation

```bash
npm install fine-use-design-system
```

## Quick Start

```jsx
import { Terminal, CodeBlock, FileTree } from 'fine-use-design-system';

function App() {
  return (
    <Terminal
      prompt="$"
      onCommand={handleCommand}
    />
  );
}
```

## Component Examples

### Terminal Component

```jsx
<Terminal
  theme="matrix"
  fontSize={14}
  promptSymbol=">"
  autocomplete={true}
/>
```

### Code Block

```jsx
<CodeBlock
  language="javascript"
  theme="monokai"
  lineNumbers={true}
  code={sourceCode}
/>
```

### File Tree

```jsx
<FileTree
  data={projectStructure}
  onSelect={handleFileSelect}
  expandedPaths={['/src']}
  showIcons={true}
/>
```

## Available Components

### Input Components
- Terminal
- CommandInput
- SearchBar
- CodeInput
- PasswordField
- AutoComplete
- CommandPalette

### Display Components
- CodeBlock
- LogViewer
- JSONViewer
- DiffViewer
- MarkdownRenderer
- SyntaxHighlighter
- DataTable
- TreeView

### Navigation
- FileExplorer
- Breadcrumbs
- TabBar
- Sidebar
- ContextMenu
- StatusBar
- ToolBar

### Feedback
- ProgressBar
- Spinner
- Toast
- Alert
- LoadingDots
- StatusLight

### Layout
- SplitPane
- Panel
- Window
- Grid
- Modal
- Drawer

## Themes

Built-in themes:
- **Classic** - Green on black terminal
- **Matrix** - Matrix-style interface
- **Dracula** - Purple and pink theme
- **Monokai** - Editor theme
- **Synthwave** - 80s neon aesthetic
- **Cyberpunk** - Futuristic glow
- **Amber** - Vintage CRT look
- **Nord** - Arctic blue palette
- **Solarized** - Easy on the eyes
- **Custom** - Define your own

## Customization

Create custom themes:

```jsx
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

## TypeScript

Full TypeScript support with type definitions:

```typescript
import { Terminal, TerminalProps } from 'fine-use-design-system';

const MyTerminal: React.FC<TerminalProps> = (props) => {
  return <Terminal {...props} />;
};
```

## Development

```bash
# Clone repository
git clone https://github.com/yourusername/fine-use-design-system
cd fine-use-design-system

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Run tests
npm test
```

## Project Structure

```
fine-use-design-system/
├── components/          # React components
├── themes/              # Theme definitions
├── documentation/       # Component docs
├── html-demos/          # Example HTML files
├── python-implementation/ # Python version (optional)
├── scripts/             # Build scripts
└── README.md            # This file
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - See [LICENSE](LICENSE) for details.

---

**Note**: This is a portfolio/demonstration project. Components may require additional testing and refinement for production use.

---

## Project Status & Roadmap

**Completion: ~30%**

### What Works
- ✅ Project structure and organization
- ✅ Documentation framework
- ✅ Conceptual design for 55 components
- ✅ README with comprehensive component list

### Known Limitations
- ❌ **No TypeScript/React Code**: 0 .tsx/.ts files found
- ❌ **Components Not Implemented**: All 55 components described but not built
- ❌ **This Is A Concept**: README describes features that don't exist

### Current Status
This appears to be a **design specification or project plan** rather than actual implementation. The README comprehensively describes 55 terminal UI components, but none are actually implemented in code.

**Recommendation**: Either build out the components or clearly label as "Design Specification" rather than working library.

**Note**: Valuable as reference for what could be built, not as usable component library.
