"use client";

import { useState } from "react";

import ReactMarkdown from "react-markdown";

import { motion } from "framer-motion";

import {
  Search,
  ShieldCheck,
  FileText,
  Sparkles
} from "lucide-react";

import {
  Card,
  CardContent,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";

import { Textarea } from "@/components/ui/textarea";

import { Badge } from "@/components/ui/badge";

import { ScrollArea } from "@/components/ui/scroll-area";

export default function Home() {

  const [topic, setTopic] = useState("");

  const [report, setReport] = useState("");

  const [status, setStatus] = useState("");

  const [loading, setLoading] = useState(false);

  const generateReport = async () => {

    setLoading(true);

    setReport("");

    const interval = setInterval(async () => {

      try {

        const statusResponse = await fetch(
          "http://127.0.0.1:8000/workflow-status"
        );

        const statusData =
          await statusResponse.json();

        setStatus(statusData.status);

      } catch (err) {

        console.error(err);
      }

    }, 1000);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/generate-report",
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({
            topic,
          }),
        }
      );

      const data = await response.json();

      setReport(data.report);

    } catch (error) {

      console.error(error);

      setReport(
        "Error generating report."
      );

    } finally {

      clearInterval(interval);

      setLoading(false);

      setStatus("Completed");
    }
  };

  return (

    <main className="min-h-screen bg-zinc-950 text-white p-6">

      <div className="mb-8">

        <h1 className="text-4xl font-bold flex items-center gap-3">

          <Sparkles className="text-blue-500" />

          AI Research Intelligence Platform

        </h1>

        <p className="text-zinc-300 mt-2">
          Multi-Agent Research + Verification + Synthesis

        </p>

      </div>

      <div className="grid grid-cols-12 gap-6">

        <div className="col-span-4 space-y-6">

          <Card className="bg-zinc-900 border border-zinc-700 text-white">

            <CardContent className="p-6 space-y-4">

              <h2 className="text-xl font-bold text-white">

                Research Topic

              </h2>

              <Textarea
                placeholder="Enter research topic..."
                value={topic}
                onChange={(e) =>
                  setTopic(e.target.value)
                }
                className="bg-zinc-950 border-zinc-700 text-white placeholder:text-zinc-500"

              />
              <Button
                onClick={generateReport}
                disabled={loading || !topic.trim()}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white disabled:bg-zinc-700 disabled:text-zinc-400"
              >

                {
                  loading
                    ? "Generating..."
                    : !topic.trim()
                      ? "Enter the research report you want to generate"
                      : "Generate Report"
                }
              </Button>

            </CardContent>

          </Card>

          <Card className="bg-zinc-900 border border-zinc-700 text-white">

            <CardContent className="p-6">

              <h2 className="text-xl font-bold text-white text-white mb-4">

                Workflow Status

              </h2>

              <div className="space-y-4">

                <div className="flex items-center gap-3">

                  <Search size={18} />

                  <span className="text-zinc-200">
                    {status}
                  </span>
                </div>

                <Badge className="bg-zinc-700 text-white">
                  LangGraph Workflow

                </Badge>

              </div>

            </CardContent>

          </Card>

        </div>

        <div className="col-span-8">

          <Card className="bg-zinc-900 border-zinc-800 h-[85vh]">

            <CardContent className="p-6 h-full">

              <div className="flex items-center justify-between mb-6">

                <h2 className="text-3xl font-bold text-white flex items-center gap-3">

                  <FileText
                    size={28}
                    className="text-blue-400"
                  />

                  Research Report

                </h2>

                <Badge className="bg-blue-600 text-white px-3 py-1">

                  AI Generated

                </Badge>

              </div>

              <ScrollArea className="h-[75vh] pr-4">

                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 0.5 }}
                >

                  <div className="prose prose-invert max-w-none text-zinc-100 prose-headings:text-white prose-p:text-zinc-200 prose-strong:text-white prose-li:text-zinc-200">
                    <ReactMarkdown>
                      {report}
                    </ReactMarkdown>

                  </div>

                </motion.div>

              </ScrollArea>

            </CardContent>

          </Card>

        </div>

      </div>

    </main>
  );
}