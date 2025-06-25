import { defineConfig } from 'rollup';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';

export default defineConfig({
  input: 'components/vanilla-js/index.js',
  output: [
    {
      file: 'dist/fine-use.esm.js',
      format: 'esm',
      sourcemap: true
    },
    {
      file: 'dist/fine-use.cjs.js',
      format: 'cjs',
      sourcemap: true
    },
    {
      file: 'dist/fine-use.umd.js',
      format: 'umd',
      name: 'FineUse',
      sourcemap: true
    },
    {
      file: 'dist/fine-use.min.js',
      format: 'umd',
      name: 'FineUse',
      sourcemap: true,
      plugins: [terser({
        compress: {
          drop_console: true,
          drop_debugger: true,
          pure_funcs: ['console.log', 'console.info']
        },
        mangle: {
          reserved: ['FineUse']
        }
      })]
    }
  ],
  plugins: [
    resolve({
      browser: true,
      preferBuiltins: false
    }),
    commonjs(),
  ],
  external: ['react', 'react-dom'],
  treeshake: {
    moduleSideEffects: false,
    propertyReadSideEffects: false,
    unknownGlobalSideEffects: false
  }
});