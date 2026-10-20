# kiln-schema

The JSON schemas of [Kiln](https://github.com/pixelpolishers/kiln-cli), a package manager for C++. They define every file format Kiln reads and writes, and are the single source of truth for the command line tool and the registry.

| Schema | Describes |
|---|---|
| `package.schema.json` | `kiln.json`: the manifest of a project or a library (dependencies, targets, build instructions, options, the build matrix, where versions come from) |
| `lock.schema.json` | `kiln.lock`: the exact versions a project resolved to |
| `assets.schema.json` | the list of prebuilt binaries of a library version, with the identity, checksum and attestation of each |
| `settings.schema.json` | the build settings of a machine (operating system, architecture, compiler, build type, linkage, ...) |

The schemas use JSON Schema draft 2020-12. `examples/` holds a library manifest, a project manifest, a lockfile and an asset list that validate against them.

## Use from Go

The schemas are embedded in a small Go package, so programs validate against exactly the files in this repository:

```go
import schemas "github.com/pixelpolishers/kiln-schema"

data, err := schemas.FS.ReadFile("package.schema.json")
```

Most programs do not use this directly: [kiln-core](https://github.com/pixelpolishers/kiln-core) wraps the schemas in a validator and typed manifests.

## Validate a file

`validate.py` checks the schemas themselves and any number of files (needs `pip install jsonschema referencing`):

```
python validate.py . package.schema.json=examples/fmt.kiln.json lock.schema.json=examples/engine.lock.json
```

It prints `OK` or `FAIL` with the reason for each file and exits with status 1 if any file fails.

## Status

Kiln is a working prototype and the formats may still change. The repository is not versioned yet.

## License

MIT, see [LICENSE](LICENSE).
