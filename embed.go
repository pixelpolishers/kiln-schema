// Package schemas embeds the JSON schemas so the registry and the CLI validate
// against exactly the files in this directory.
package schemas

import "embed"

//go:embed *.schema.json
var FS embed.FS
