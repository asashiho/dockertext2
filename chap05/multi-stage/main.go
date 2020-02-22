package main

import (
	"fmt"
	"os"

	"github.com/urfave/cli"
)

func main() {
	app := cli.NewApp()
	app.Name = "Greeting"
	app.Version = "1.0.0"

	app.Flags = []cli.Flag{
		&cli.StringFlag{
			Name:  "lang",
			Value: "en",
			Usage: "language for the greeting(es/fr/en)",
		},
	}

	app.Action = func(c *cli.Context) error {
		name := "world!"
		if c.NArg() > 0 {
			name = c.Args().Get(0)
		}
		if c.String("lang") == "es" {
			fmt.Println("Hola", name)
		} else if c.String("lang") == "fr" {
			fmt.Println("Bonjour", name)
		} else {
			fmt.Println("Hello", name)
		}
		return nil
	}

	app.Run(os.Args)
}
